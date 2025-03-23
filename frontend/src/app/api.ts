import { Curriculum } from './types';

// API Configuration
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8080';

// Add logging for API URL
console.log('Using API URL:', API_URL);

// Cache for curriculum data
let curriculumCache: Curriculum | null = null;
let lastFetchTime = 0;
const CACHE_DURATION = 60000; // 1 minute in milliseconds

export async function fetchCurriculum() {
  const now = Date.now();
  
  // Return cached data if it's still valid
  if (curriculumCache && (now - lastFetchTime) < CACHE_DURATION) {
    return curriculumCache;
  }

  try {
    console.log('Fetching curriculum from:', API_URL);
    const response = await fetch(`${API_URL}/curriculum`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('API Error:', {
        status: response.status,
        statusText: response.statusText,
        body: errorText,
        url: `${API_URL}/curriculum`
      });
      throw new Error(`Failed to fetch curriculum: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    curriculumCache = data;
    lastFetchTime = now;
    return data;
  } catch (error) {
    console.error('Error fetching curriculum:', error);
    throw error;
  }
}

export async function updateTopicStatus(moduleId: number, topicId: number, status: string) {
  try {
    const url = `${API_URL}/curriculum/module/${moduleId}/topic/${topicId}/status?status=${status}`;
    console.log('Updating topic status:', url);
    
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {
      const errorText = await response.text();
      console.error('API Error:', {
        status: response.status,
        statusText: response.statusText,
        body: errorText,
        url
      });
      throw new Error(`Failed to update topic status: ${response.status} ${response.statusText}`);
    }
    
    // Invalidate cache
    curriculumCache = null;
    return await fetchCurriculum();
  } catch (error) {
    console.error('Error updating topic status:', error);
    throw error;
  }
}

export async function updateSubtopicStatus(moduleId: number, topicId: number, subtopicId: number, status: string) {
  const MAX_RETRIES = 3;
  const RETRY_DELAY = 1000; // 1 second

  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      // Validate inputs
      if (!moduleId || !topicId || !subtopicId || !status) {
        throw new Error('Missing required parameters');
      }

      // For Module 1, handle subtopic IDs specially
      let finalSubtopicId = subtopicId;
      if (moduleId === 1) {
        // If the subtopic ID is already prefixed (e.g., 201), use it as is
        // If it's not prefixed (e.g., 1), prefix it with the topic ID
        const subtopicIdStr = String(subtopicId);
        if (subtopicIdStr.length <= 2) {
          finalSubtopicId = parseInt(`${topicId}${subtopicIdStr.padStart(2, '0')}`);
        }
      }

      const url = `${API_URL}/curriculum/module/${moduleId}/topic/${topicId}/subtopic/${finalSubtopicId}/status?status=${status}`;
      
      console.log(`Attempt ${attempt}/${MAX_RETRIES} - Updating subtopic status:`, {
        moduleId,
        topicId,
        originalSubtopicId: subtopicId,
        finalSubtopicId,
        status,
        url
      });

      const response = await fetch(url, {
        method: 'PUT',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error(`Attempt ${attempt}/${MAX_RETRIES} - Failed to update subtopic status:`, {
          status: response.status,
          statusText: response.statusText,
          body: errorText,
          url,
          params: {
            moduleId,
            topicId,
            originalSubtopicId: subtopicId,
            finalSubtopicId,
            status
          }
        });

        // If it's a 502 error and we haven't exhausted retries, wait and try again
        if (response.status === 502 && attempt < MAX_RETRIES) {
          console.log(`Waiting ${RETRY_DELAY}ms before retry...`);
          await new Promise(resolve => setTimeout(resolve, RETRY_DELAY));
          continue;
        }

        throw new Error(`Failed to update subtopic status: ${response.status} ${response.statusText}`);
      }

      // Invalidate cache and fetch fresh data
      curriculumCache = null;
      return await fetchCurriculum();
    } catch (error) {
      console.error(`Attempt ${attempt}/${MAX_RETRIES} - Error in updateSubtopicStatus:`, error);
      
      // If this is the last attempt, throw the error
      if (attempt === MAX_RETRIES) {
        throw error;
      }
      
      // Otherwise, wait and try again
      console.log(`Waiting ${RETRY_DELAY}ms before retry...`);
      await new Promise(resolve => setTimeout(resolve, RETRY_DELAY));
    }
  }
} 
import { Curriculum } from './types';

// Get the API URL from environment variable or use default
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://curriculum-tracker-new-backend.onrender.com';

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
  try {
    console.log('%c API CALL DEBUG', 'background: #0000ff; color: white; font-size: 16px;');
    
    // For Module 1, subtopic IDs are prefixed with topic ID (e.g., 101, 102, 201, 202)
    // For other modules, subtopic IDs are simple sequential numbers (1, 2, 3)
    let adjustedSubtopicId = subtopicId;
    
    if (moduleId === 1) {
      // If the subtopic ID is already prefixed (e.g., 201), use it as is
      // If it's not prefixed (e.g., 1), prefix it with the topic ID
      if (String(subtopicId).length <= 2) {
        adjustedSubtopicId = parseInt(String(topicId) + String(subtopicId).padStart(2, '0'));
      }
    }
    
    const url = `${API_URL}/curriculum/module/${moduleId}/topic/${topicId}/subtopic/${adjustedSubtopicId}/status?status=${status}`;
    console.log('Making API call to update subtopic status:', {
      url,
      API_URL,
      params: {
        moduleId,
        topicId,
        originalSubtopicId: subtopicId,
        adjustedSubtopicId,
        status,
        isModule1: moduleId === 1,
        idLength: String(subtopicId).length,
        needsPrefix: moduleId === 1 && String(subtopicId).length <= 2
      }
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
      console.error('%c API ERROR', 'background: #ff0000; color: white; font-size: 16px;');
      console.error('API Error:', {
        status: response.status,
        statusText: response.statusText,
        body: errorText,
        url,
        API_URL,
        params: {
          moduleId,
          topicId,
          originalSubtopicId: subtopicId,
          adjustedSubtopicId,
          status,
          isModule1: moduleId === 1,
          idLength: String(subtopicId).length,
          needsPrefix: moduleId === 1 && String(subtopicId).length <= 2
        }
      });
      throw new Error(`Failed to update subtopic status: ${response.status} ${response.statusText}`);
    }

    console.log('%c API SUCCESS', 'background: #00ff00; color: black; font-size: 16px;');
    console.log('Subtopic status updated successfully');
    
    // Invalidate cache
    curriculumCache = null;
    return await fetchCurriculum();
  } catch (error) {
    console.error('Error updating subtopic status:', error);
    throw error;
  }
} 
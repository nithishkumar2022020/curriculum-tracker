import { Curriculum } from './types';

// Get the API URL from environment variable or use default
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://curriculum-tracker-backend.onrender.com';

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
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
      },
      mode: 'cors', // Explicitly set CORS mode
      credentials: 'include', // Include credentials if needed
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
      mode: 'cors', // Explicitly set CORS mode
      credentials: 'include', // Include credentials if needed
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
    const url = `${API_URL}/curriculum/module/${moduleId}/topic/${topicId}/subtopic/${subtopicId}/status?status=${status}`;
    console.log('Updating subtopic status:', url);
    
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      mode: 'cors', // Explicitly set CORS mode
      credentials: 'include', // Include credentials if needed
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('API Error:', {
        status: response.status,
        statusText: response.statusText,
        body: errorText,
        url
      });
      throw new Error(`Failed to update subtopic status: ${response.status} ${response.statusText}`);
    }

    // Invalidate cache
    curriculumCache = null;
    return await fetchCurriculum();
  } catch (error) {
    console.error('Error updating subtopic status:', error);
    throw error;
  }
} 
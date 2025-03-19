const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://curriculum-tracker-backend.onrender.com';

// Cache for curriculum data
let curriculumCache: any = null;
let lastFetchTime = 0;
const CACHE_DURATION = 60000; // 1 minute in milliseconds

export async function fetchCurriculum() {
  const now = Date.now();
  
  // Return cached data if it's still valid
  if (curriculumCache && (now - lastFetchTime) < CACHE_DURATION) {
    return curriculumCache;
  }

  try {
    const response = await fetch(`${API_URL}/curriculum`, {
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to fetch curriculum: ${response.statusText}`);
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
    const response = await fetch(
      `${API_URL}/curriculum/module/${moduleId}/topic/${topicId}/status?status=${status}`,
      {
        method: 'PUT',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
      }
    );
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
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
    const backendSubtopicId = topicId * 100 + subtopicId;
    
    const response = await fetch(
      `${API_URL}/curriculum/module/${moduleId}/topic/${topicId}/subtopic/${backendSubtopicId}/status?status=${status}`,
      {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );

    if (!response.ok) {
      throw new Error(`Failed to update subtopic status: ${response.statusText}`);
    }

    // Invalidate cache
    curriculumCache = null;
    return await fetchCurriculum();
  } catch (error) {
    console.error('Error updating subtopic status:', error);
    throw error;
  }
} 
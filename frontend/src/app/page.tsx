'use client';

import { useEffect, useState } from 'react';
import { fetchCurriculum, updateTopicStatus, updateSubtopicStatus } from './api';
import { Curriculum, Module, Topic, Subtopic } from './types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://curriculum-tracker-backend.onrender.com';

export default function Home() {
  const [curriculum, setCurriculum] = useState<Curriculum | null>(null);
  const [loading, setLoading] = useState(true);
  const [expandedModules, setExpandedModules] = useState<Record<number, boolean>>({});
  const [expandedTopics, setExpandedTopics] = useState<Record<string, boolean>>({});
  const [error, setError] = useState<string | null>(null);

  // Toggle module expansion
  const toggleModule = (moduleId: number) => {
    setExpandedModules(prev => ({
      ...prev,
      [moduleId]: !prev[moduleId]
    }));
  };

  // Toggle topic expansion
  const toggleTopic = (moduleId: number, topicId: number) => {
    const key = `${moduleId}-${topicId}`;
    setExpandedTopics(prev => ({
      ...prev,
      [key]: !prev[key]
    }));
  };

  // Color schemes for each module to improve visual distinction
  const moduleColors = {
    1: { bg: 'bg-indigo-600', ringBg: 'bg-indigo-950', ringBorder: 'border-indigo-800', text: 'text-indigo-300' },
    2: { bg: 'bg-fuchsia-600', ringBg: 'bg-fuchsia-950', ringBorder: 'border-fuchsia-800', text: 'text-fuchsia-300' },
    3: { bg: 'bg-emerald-600', ringBg: 'bg-emerald-950', ringBorder: 'border-emerald-800', text: 'text-emerald-300' },
    4: { bg: 'bg-amber-600', ringBg: 'bg-amber-950', ringBorder: 'border-amber-800', text: 'text-amber-300' },
    5: { bg: 'bg-rose-600', ringBg: 'bg-rose-950', ringBorder: 'border-rose-800', text: 'text-rose-300' },
  };

  // Get color scheme for a module
  const getModuleColor = (moduleId: number) => {
    return moduleColors[moduleId as keyof typeof moduleColors] || 
           { bg: 'bg-violet-600', ringBg: 'bg-violet-950', ringBorder: 'border-violet-800', text: 'text-violet-300' };
  };

  useEffect(() => {
    const loadCurriculum = async () => {
      try {
        setLoading(true);
        const data = await fetchCurriculum();
        setCurriculum(data);
      } catch (error) {
        console.error('Error loading curriculum:', error);
        setError('Failed to load curriculum data');
      } finally {
        setLoading(false);
      }
    };

    loadCurriculum();
  }, []);

  const handleTopicStatusUpdate = async (moduleId: number, topicId: number, status: string) => {
    try {
      const data = await updateTopicStatus(moduleId, topicId, status);
      setCurriculum(data);
    } catch (error) {
      console.error('Error updating topic status:', error);
    }
  };

  const handleSubtopicStatusUpdate = async (moduleId: number, topicId: number, subtopicId: number, status: string) => {
    try {
      const data = await updateSubtopicStatus(moduleId, topicId, subtopicId, status);
      setCurriculum(data);
    } catch (error) {
      console.error('Error updating subtopic status:', error);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-[#050505]">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-white"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-12 bg-[#050505]">
        <h2 className="text-2xl font-semibold text-white mb-4">Error loading curriculum</h2>
        <p className="text-red-400">{error}</p>
        <button 
          onClick={() => window.location.reload()} 
          className="mt-4 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 rounded text-white transition-colors"
        >
          Retry
        </button>
      </div>
    );
  }

  if (!curriculum) {
    return (
      <div className="text-center py-12 bg-[#050505]">
        <h2 className="text-2xl font-semibold text-white">Error loading curriculum</h2>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#050505] text-gray-200">
      <div className="max-w-7xl mx-auto p-6 space-y-8 bg-[#050505]">
        <h1 className="text-3xl font-bold text-white mb-8">Full-Stack Progress Tracker</h1>
        
        {/* Overall Progress */}
        <div className="bg-[#0c0c0c] rounded-lg shadow-xl p-6 border border-gray-800">
          <h2 className="text-2xl font-bold text-white mb-4">Overall Progress</h2>
          <div className="relative pt-1">
            <div className="flex mb-2 items-center justify-between">
              <div>
                <span className="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-violet-300 bg-violet-950 border border-violet-800">
                  {(curriculum?.total_progress || 0).toFixed(1)}% Complete
                </span>
              </div>
            </div>
            <div className="overflow-hidden h-2 mb-4 text-xs flex rounded bg-[#161616]">
              <div
                style={{ width: `${curriculum.total_progress}%` }}
                className="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-violet-600 transition-all duration-500"
              ></div>
            </div>
          </div>
        </div>

        {/* Modules */}
        <div className="space-y-6">
          {curriculum.modules.map((module) => {
            const colors = getModuleColor(module.id);
            const isExpanded = expandedModules[module.id] !== false; // Default to expanded
            
            return (
              <div key={module.id} className="bg-[#0c0c0c] rounded-lg shadow-xl overflow-hidden border border-gray-800 transition-all duration-300">
                <div 
                  className="px-6 py-4 border-b border-gray-800 bg-[#080808] cursor-pointer hover:bg-[#0f0f0f]"
                  onClick={() => toggleModule(module.id)}
                >
                  <div className="flex justify-between items-center">
                    <div className="flex items-center space-x-2">
                      <div className={`transform transition-transform ${isExpanded ? 'rotate-90' : ''}`}>
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                        </svg>
                      </div>
                      <h3 className="text-xl font-semibold text-white">{module.name}</h3>
                    </div>
                    <span className="text-sm text-gray-400">{module.duration}</span>
                  </div>
                  <p className="mt-1 text-sm text-gray-400 ml-7">{module.description}</p>
                  <div className="mt-3 ml-7">
                    <div className="relative pt-1">
                      <div className="flex mb-2 items-center justify-between">
                        <div>
                          <span className={`text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full ${colors.text} ${colors.ringBg} border ${colors.ringBorder}`}>
                            {(module?.progress || 0).toFixed(1)}% Complete
                          </span>
                        </div>
                      </div>
                      <div className="overflow-hidden h-2 mb-1 text-xs flex rounded bg-[#161616]">
                        <div
                          style={{ width: `${module.progress}%` }}
                          className={`shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center ${colors.bg} transition-all duration-500`}
                        ></div>
                      </div>
                    </div>
                  </div>
                </div>
                
                {isExpanded && (
                  <div className="p-6 space-y-6 bg-[#0a0a0a]">
                    {module.topics.map((topic) => {
                      const topicKey = `${module.id}-${topic.id}`;
                      const isTopicExpanded = expandedTopics[topicKey] !== false; // Default to expanded
                      
                      return (
                        <div
                          key={topic.id}
                          className="bg-[#080808] rounded-lg border border-gray-800 overflow-hidden transition-all duration-300 shadow-md"
                        >
                          <div 
                            className="p-4 cursor-pointer hover:bg-[#0c0c0c]"
                            onClick={() => toggleTopic(module.id, topic.id)}
                          >
                            <div className="flex flex-col space-y-3">
                              <div className="flex items-center justify-between">
                                <div className="flex-1 flex items-center space-x-2">
                                  <div className={`transform transition-transform ${isTopicExpanded ? 'rotate-90' : ''}`}>
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                                    </svg>
                                  </div>
                                  <div>
                                    <h4 className="text-lg font-medium text-white">{topic.name}</h4>
                                    <p className="text-sm text-gray-400">{topic.description}</p>
                                    <div className="flex items-center space-x-4 mt-1">
                                      <span className="text-xs text-gray-500">{topic.duration}</span>
                                      {topic.completed_date && (
                                        <span className="text-xs text-green-400">
                                          Completed: {new Date(topic.completed_date).toLocaleDateString()}
                                        </span>
                                      )}
                                    </div>
                                  </div>
                                </div>
                                <div className="flex space-x-2">
                                  <button
                                    onClick={(e) => {
                                      e.stopPropagation();
                                      handleTopicStatusUpdate(module.id, topic.id, 'not_started');
                                    }}
                                    className={`px-3 py-1 rounded-full text-xs font-semibold transition-all duration-200 ${
                                      topic.status === 'not_started'
                                        ? 'bg-gray-700 text-white ring-2 ring-gray-600'
                                        : 'bg-[#121212] text-gray-400 hover:bg-gray-700 hover:text-white'
                                    }`}
                                  >
                                    Not Started
                                  </button>
                                  <button
                                    onClick={(e) => {
                                      e.stopPropagation();
                                      handleTopicStatusUpdate(module.id, topic.id, 'in_progress');
                                    }}
                                    className={`px-3 py-1 rounded-full text-xs font-semibold transition-all duration-200 ${
                                      topic.status === 'in_progress'
                                        ? 'bg-blue-900 text-blue-100 ring-2 ring-blue-700'
                                        : 'bg-[#121212] text-gray-400 hover:bg-blue-900 hover:text-blue-100'
                                    }`}
                                  >
                                    In Progress
                                  </button>
                                  <button
                                    onClick={(e) => {
                                      e.stopPropagation();
                                      handleTopicStatusUpdate(module.id, topic.id, 'completed');
                                    }}
                                    className={`px-3 py-1 rounded-full text-xs font-semibold transition-all duration-200 ${
                                      topic.status === 'completed'
                                        ? 'bg-green-900 text-green-100 ring-2 ring-green-700'
                                        : 'bg-[#121212] text-gray-400 hover:bg-green-900 hover:text-green-100'
                                    }`}
                                  >
                                    Completed
                                  </button>
                                </div>
                              </div>
                            </div>
                          </div>
                          
                          {/* Subtopics with granular progress */}
                          {isTopicExpanded && topic.subtopics && topic.subtopics.length > 0 && (
                            <div className="border-t border-gray-800 bg-[#060606] p-4 space-y-3">
                              <h5 className="text-sm font-medium text-gray-400 mb-3">Detailed Progress:</h5>
                              {topic.subtopics.map((subtopic) => (
                                <div
                                  key={subtopic.id}
                                  className="bg-[#0c0c0c] rounded-lg border border-gray-800 p-3 shadow-sm"
                                >
                                  <div className="flex flex-col space-y-2">
                                    <div className="flex items-center justify-between">
                                      <div className="flex-1">
                                        <h6 className="text-sm font-medium text-white">{subtopic.name}</h6>
                                        <p className="text-xs text-gray-400">{subtopic.description}</p>
                                        <div className="flex items-center space-x-4 mt-1">
                                          <span className="text-xs text-gray-500">{subtopic.duration}</span>
                                          {subtopic.completed_date && (
                                            <span className="text-xs text-green-400">
                                              Completed: {new Date(subtopic.completed_date).toLocaleDateString()}
                                            </span>
                                          )}
                                        </div>
                                      </div>
                                      <div className="flex space-x-2">
                                        <button
                                          onClick={(e) => {
                                            e.stopPropagation();
                                            handleSubtopicStatusUpdate(module.id, topic.id, subtopic.id, 'not_started');
                                          }}
                                          className={`px-2 py-1 rounded-full text-xs font-semibold transition-all duration-200 ${
                                            subtopic.status === 'not_started'
                                              ? 'bg-gray-700 text-white ring-2 ring-gray-600'
                                              : 'bg-[#121212] text-gray-400 hover:bg-gray-700 hover:text-white'
                                          }`}
                                        >
                                          Not Started
                                        </button>
                                        <button
                                          onClick={(e) => {
                                            e.stopPropagation();
                                            handleSubtopicStatusUpdate(module.id, topic.id, subtopic.id, 'in_progress');
                                          }}
                                          className={`px-2 py-1 rounded-full text-xs font-semibold transition-all duration-200 ${
                                            subtopic.status === 'in_progress'
                                              ? 'bg-blue-900 text-blue-100 ring-2 ring-blue-700'
                                              : 'bg-[#121212] text-gray-400 hover:bg-blue-900 hover:text-blue-100'
                                          }`}
                                        >
                                          In Progress
                                        </button>
                                        <button
                                          onClick={(e) => {
                                            e.stopPropagation();
                                            handleSubtopicStatusUpdate(module.id, topic.id, subtopic.id, 'completed');
                                          }}
                                          className={`px-2 py-1 rounded-full text-xs font-semibold transition-all duration-200 ${
                                            subtopic.status === 'completed'
                                              ? 'bg-green-900 text-green-100 ring-2 ring-green-700'
                                              : 'bg-[#121212] text-gray-400 hover:bg-green-900 hover:text-green-100'
                                          }`}
                                        >
                                          Completed
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              ))}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

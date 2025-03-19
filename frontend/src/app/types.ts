export interface Subtopic {
  id: number;
  name: string;
  description: string;
  duration: string;
  status: string;
  completed_date: string | null;
}

export interface Topic {
  id: number;
  name: string;
  description: string;
  duration: string;
  status: string;
  completed_date: string | null;
  subtopics: Subtopic[];
}

export interface Module {
  id: number;
  name: string;
  description: string;
  duration: string;
  topics: Topic[];
  status: string;
  progress: number;
}

export interface Curriculum {
  id: number;
  name: string;
  description: string;
  modules: Module[];
  total_progress: number;
} 
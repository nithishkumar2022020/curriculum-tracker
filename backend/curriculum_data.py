from typing import Dict, Any
from datetime import datetime

def get_curriculum_data() -> Dict[str, Any]:
    return {
        "id": 1,
        "name": "Full-Stack Development Curriculum",
        "description": "Comprehensive 9-12 month curriculum for full-stack development",
        "total_progress": 0.0,
        "modules": [
            {
                "id": 1,
                "name": "Backend Development with Python",
                "description": "8 weeks of Python backend development",
                "duration": "8 weeks",
                "progress": 0.0,
                "status": "not_started",
                "topics": [
                    {
                        "id": 1,
                        "name": "Python Fundamentals (Weeks 1-2)",
                        "description": "Core syntax, data types, control flow, OOP, and API basics",
                        "duration": "2 weeks",
                        "status": "not_started",
                        "completed_date": None,
                        "subtopics": [
                            {
                                "id": 101,  # Prefixed with topic ID (1)
                                "name": "Python Syntax & Data Types",
                                "description": "Basic syntax, variables, data types, control flow",
                                "duration": "3 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 102,  # Prefixed with topic ID (1)
                                "name": "Functions & Modules",
                                "description": "Function definitions, modules, packages, error handling",
                                "duration": "2 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 103,  # Prefixed with topic ID (1)
                                "name": "Object-Oriented Programming",
                                "description": "Classes, inheritance, polymorphism, encapsulation",
                                "duration": "3 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 104,  # Prefixed with topic ID (1)
                                "name": "Testing & Debugging",
                                "description": "Unit testing with pytest, debugging techniques",
                                "duration": "2 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 105,  # Prefixed with topic ID (1)
                                "name": "REST API Basics",
                                "description": "Introduction to REST API design, FastAPI/Flask basics",
                                "duration": "2 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 106,  # Prefixed with topic ID (1)
                                "name": "Weather API Project",
                                "description": "Build a weather API with caching functionality",
                                "duration": "3 days",
                                "status": "not_started",
                                "completed_date": None
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "name": "Database Engineering (Weeks 3-5)",
                        "description": "SQL, PostgreSQL, ORMs, and NoSQL databases",
                        "duration": "3 weeks",
                        "status": "not_started",
                        "completed_date": None,
                        "subtopics": [
                            {
                                "id": 201,  # Prefixed with topic ID (2)
                                "name": "SQL Fundamentals",
                                "description": "Queries, joins, normalization, indexing",
                                "duration": "5 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 202,  # Prefixed with topic ID (2)
                                "name": "PostgreSQL",
                                "description": "Setup, schema design, migrations",
                                "duration": "5 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 203,  # Prefixed with topic ID (2)
                                "name": "ORM & Database Design",
                                "description": "Django ORM/SQLAlchemy, database interactions",
                                "duration": "5 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 204,  # Prefixed with topic ID (2)
                                "name": "MongoDB Basics",
                                "description": "CRUD operations, aggregation pipelines",
                                "duration": "5 days",
                                "status": "not_started",
                                "completed_date": None
                            },
                            {
                                "id": 205,  # Prefixed with topic ID (2)
                                "name": "Library Management Project",
                                "description": "Build a system using both SQL and NoSQL",
                                "duration": "5 days",
                                "status": "not_started",
                                "completed_date": None
                            }
                        ]
                    }
                ]
            }
        ]
    }

def find_subtopic(module_id: int, topic_id: int, subtopic_id: int) -> Dict[str, Any]:
    curriculum = get_curriculum_data()
    
    # Find the module
    module = next((m for m in curriculum["modules"] if m["id"] == module_id), None)
    if not module:
        print(f"Module {module_id} not found")
        return None
    
    # Find the topic
    topic = next((t for t in module["topics"] if t["id"] == topic_id), None)
    if not topic:
        print(f"Topic {topic_id} not found in module {module_id}")
        return None
    
    # For Module 1, handle subtopic IDs specially
    if module_id == 1:
        # If the subtopic ID is already prefixed, verify it matches the topic ID
        subtopic_id_str = str(subtopic_id)
        if len(subtopic_id_str) > 2:
            prefix = subtopic_id_str[0]
            if prefix != str(topic_id):
                print(f"Invalid subtopic ID: {subtopic_id} does not match topic ID {topic_id}")
                return None
        else:
            # If not prefixed, prefix it with the topic ID
            subtopic_id = int(f"{topic_id}{subtopic_id_str.padStart(2, '0')}")
            print(f"Adjusted subtopic ID: {subtopic_id}")
    
    # Find the subtopic
    subtopic = next((s for s in topic["subtopics"] if s["id"] == subtopic_id), None)
    if not subtopic:
        print(f"Subtopic {subtopic_id} not found in topic {topic_id} of module {module_id}")
        print(f"Available subtopics: {[s['id'] for s in topic['subtopics']]}")
    return subtopic 
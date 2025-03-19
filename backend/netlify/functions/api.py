import json
from datetime import datetime

# Sample Curriculum Data
curriculum_data = {
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
                            "id": 101,
                            "name": "Python Syntax & Data Types",
                            "description": "Basic syntax, variables, data types, control flow",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 102,
                            "name": "Functions & Modules",
                            "description": "Function definitions, arguments, return values, modules",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 103,
                            "name": "Object-Oriented Programming",
                            "description": "Classes, objects, inheritance, polymorphism",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 104,
                            "name": "Error Handling & File I/O",
                            "description": "Try-except blocks, file operations",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Web Development with Flask (Weeks 3-4)",
                    "description": "Building web applications using Flask framework",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 201,
                            "name": "Flask Basics",
                            "description": "Routes, views, templates",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 202,
                            "name": "Database Integration",
                            "description": "SQLAlchemy, models, migrations",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 203,
                            "name": "Authentication & Authorization",
                            "description": "User management, login/logout, permissions",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 204,
                            "name": "RESTful APIs",
                            "description": "API design, endpoints, serialization",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 2,
            "name": "Frontend Development",
            "description": "12 weeks of frontend development",
            "duration": "12 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 3,
                    "name": "HTML & CSS Fundamentals (Weeks 1-3)",
                    "description": "Building blocks of web development",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 301,
                            "name": "HTML5 Basics",
                            "description": "Document structure, elements, forms",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 302,
                            "name": "CSS3 Styling",
                            "description": "Selectors, box model, layouts",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 303,
                            "name": "Responsive Design",
                            "description": "Media queries, flexbox, grid",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 4,
                    "name": "JavaScript & Modern Web (Weeks 4-8)",
                    "description": "Core JavaScript and modern web development",
                    "duration": "5 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 401,
                            "name": "JavaScript Fundamentals",
                            "description": "Syntax, functions, DOM manipulation",
                            "duration": "2 weeks",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 402,
                            "name": "ES6+ Features",
                            "description": "Modern JavaScript features and syntax",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 403,
                            "name": "Async Programming",
                            "description": "Promises, async/await, fetch API",
                            "duration": "2 weeks",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 5,
                    "name": "React Development (Weeks 9-12)",
                    "description": "Building modern web applications with React",
                    "duration": "4 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 501,
                            "name": "React Basics",
                            "description": "Components, props, state",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 502,
                            "name": "React Hooks",
                            "description": "useState, useEffect, custom hooks",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 503,
                            "name": "State Management",
                            "description": "Context API, Redux basics",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 504,
                            "name": "React Router & APIs",
                            "description": "Routing, API integration",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 3,
            "name": "Database Management",
            "description": "6 weeks of database design and management",
            "duration": "6 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 6,
                    "name": "SQL Fundamentals (Weeks 1-2)",
                    "description": "Core SQL concepts and database design",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 601,
                            "name": "Database Design",
                            "description": "ERD, normalization, relationships",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 602,
                            "name": "SQL Queries",
                            "description": "SELECT, INSERT, UPDATE, DELETE",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 603,
                            "name": "Advanced SQL",
                            "description": "Joins, subqueries, indexes",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 7,
                    "name": "NoSQL Databases (Weeks 3-4)",
                    "description": "MongoDB and document databases",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 701,
                            "name": "MongoDB Basics",
                            "description": "Documents, collections, CRUD operations",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 702,
                            "name": "Advanced MongoDB",
                            "description": "Aggregation, indexing, optimization",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 8,
                    "name": "Database Administration (Weeks 5-6)",
                    "description": "Management, optimization, and security",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 801,
                            "name": "Performance Tuning",
                            "description": "Query optimization, indexing strategies",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 802,
                            "name": "Backup & Recovery",
                            "description": "Backup strategies, disaster recovery",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 803,
                            "name": "Security",
                            "description": "Authentication, authorization, encryption",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 4,
            "name": "DevOps & Deployment",
            "description": "4 weeks of DevOps practices and deployment",
            "duration": "4 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 9,
                    "name": "Version Control & Git (Week 1)",
                    "description": "Source control and collaboration",
                    "duration": "1 week",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 901,
                            "name": "Git Basics",
                            "description": "Repositories, commits, branches",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 902,
                            "name": "Collaboration",
                            "description": "Pull requests, merge conflicts",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 10,
                    "name": "CI/CD (Week 2)",
                    "description": "Continuous Integration and Deployment",
                    "duration": "1 week",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1001,
                            "name": "CI Pipelines",
                            "description": "Build automation, testing",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1002,
                            "name": "CD Practices",
                            "description": "Deployment strategies, monitoring",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 11,
                    "name": "Cloud Services (Weeks 3-4)",
                    "description": "AWS and cloud deployment",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1101,
                            "name": "AWS Basics",
                            "description": "EC2, S3, RDS services",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1102,
                            "name": "Serverless",
                            "description": "Lambda, API Gateway",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 5,
            "name": "System Design & Architecture",
            "description": "4 weeks of system design principles",
            "duration": "4 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 12,
                    "name": "Design Patterns (Weeks 1-2)",
                    "description": "Common software design patterns",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1201,
                            "name": "Creational Patterns",
                            "description": "Singleton, Factory, Builder patterns",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1202,
                            "name": "Structural Patterns",
                            "description": "Adapter, Decorator, Facade patterns",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1203,
                            "name": "Behavioral Patterns",
                            "description": "Observer, Strategy, Command patterns",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 13,
                    "name": "Microservices (Weeks 3-4)",
                    "description": "Distributed system architecture",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1301,
                            "name": "Architecture Patterns",
                            "description": "Service decomposition, API design",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1302,
                            "name": "Service Communication",
                            "description": "REST, gRPC, message queues",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1303,
                            "name": "Monitoring & Scaling",
                            "description": "Logging, metrics, auto-scaling",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        }
    ]
}

def handle_get_curriculum():
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS"
        },
        "body": json.dumps(curriculum_data)
    }

def handle_update_topic_status(module_id, topic_id, status):
    if status not in ["not_started", "in_progress", "completed"]:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Invalid status value"})
        }
    
    topic_found = False
    for module in curriculum_data["modules"]:
        if module["id"] == module_id:
            for topic in module["topics"]:
                if topic["id"] == topic_id:
                    topic_found = True
                    topic["status"] = status
                    if status == "completed":
                        topic["completed_date"] = datetime.now().isoformat()
                        for subtopic in topic.get("subtopics", []):
                            subtopic["status"] = "completed"
                            subtopic["completed_date"] = datetime.now().isoformat()
                    elif status == "not_started":
                        topic["completed_date"] = None
                        for subtopic in topic.get("subtopics", []):
                            subtopic["status"] = "not_started"
                            subtopic["completed_date"] = None
                    
                    # Update progress calculations
                    if topic.get("subtopics"):
                        total_subtopics = len(topic["subtopics"])
                        completed_subtopics = sum(1 for s in topic["subtopics"] if s["status"] == "completed")
                        topic["progress"] = (completed_subtopics / total_subtopics) * 100
                    else:
                        topic["progress"] = 100 if status == "completed" else 0
                    
                    # Update module progress
                    total_topics = len(module["topics"])
                    module_progress = sum(t.get("progress", 0) for t in module["topics"])
                    module["progress"] = module_progress / total_topics
                    
                    # Update overall curriculum progress
                    total_modules = len(curriculum_data["modules"])
                    total_progress = sum(m["progress"] for m in curriculum_data["modules"])
                    curriculum_data["total_progress"] = total_progress / total_modules
                    
                    return {
                        "statusCode": 200,
                        "headers": {
                            "Content-Type": "application/json",
                            "Access-Control-Allow-Origin": "*"
                        },
                        "body": json.dumps({"message": "Status updated successfully"})
                    }
    
    if not topic_found:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Topic not found"})
        }
    
    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"error": "Internal server error"})
    }

def handle_update_subtopic_status(module_id, topic_id, subtopic_id, status):
    if status not in ["not_started", "in_progress", "completed"]:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Invalid status value"})
        }
    
    subtopic_found = False
    for module in curriculum_data["modules"]:
        if module["id"] == module_id:
            for topic in module["topics"]:
                if topic["id"] == topic_id:
                    for subtopic in topic.get("subtopics", []):
                        if subtopic["id"] == subtopic_id:
                            subtopic_found = True
                            subtopic["status"] = status
                            if status == "completed":
                                subtopic["completed_date"] = datetime.now().isoformat()
                            elif status == "not_started":
                                subtopic["completed_date"] = None
                            
                            # Update topic progress
                            total_subtopics = len(topic["subtopics"])
                            completed_subtopics = sum(1 for s in topic["subtopics"] if s["status"] == "completed")
                            topic["progress"] = (completed_subtopics / total_subtopics) * 100
                            
                            # Update topic status
                            if all(s["status"] == "completed" for s in topic["subtopics"]):
                                topic["status"] = "completed"
                                topic["completed_date"] = datetime.now().isoformat()
                            elif any(s["status"] == "in_progress" for s in topic["subtopics"]):
                                topic["status"] = "in_progress"
                            else:
                                topic["status"] = "not_started"
                                topic["completed_date"] = None
                            
                            # Update module progress
                            total_topics = len(module["topics"])
                            module_progress = sum(t.get("progress", 0) for t in module["topics"])
                            module["progress"] = module_progress / total_topics
                            
                            # Update overall curriculum progress
                            total_modules = len(curriculum_data["modules"])
                            total_progress = sum(m["progress"] for m in curriculum_data["modules"])
                            curriculum_data["total_progress"] = total_progress / total_modules
                            
                            return {
                                "statusCode": 200,
                                "headers": {
                                    "Content-Type": "application/json",
                                    "Access-Control-Allow-Origin": "*"
                                },
                                "body": json.dumps({"message": "Status updated successfully"})
                            }
    
    if not subtopic_found:
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Subtopic not found"})
        }
    
    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"error": "Internal server error"})
    }

def handler(event, context):
    # Handle CORS preflight requests
    if event["httpMethod"] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS"
            }
        }

    # Handle GET requests
    if event["httpMethod"] == "GET":
        path = event.get("path", "")
        if path == "/curriculum" or path == "/api/curriculum" or path.endswith("/curriculum"):
            return handle_get_curriculum()
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Not found"})
        }

    # Handle PUT requests
    if event["httpMethod"] == "PUT":
        try:
            data = json.loads(event["body"])
            path = event.get("path", "")
            
            if "/curriculum/module/" in path or "/api/curriculum/module/" in path:
                path_parts = path.split("/")
                module_id = int(path_parts[-3])
                topic_id = int(path_parts[-1])
                
                if "subtopic" in path:
                    subtopic_id = int(path_parts[-1])
                    return handle_update_subtopic_status(module_id, topic_id, subtopic_id, data["status"])
                else:
                    return handle_update_topic_status(module_id, topic_id, data["status"])
            
            return {
                "statusCode": 404,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": "Not found"})
            }
        except Exception as e:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": str(e)})
            }

    return {
        "statusCode": 405,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"error": "Method not allowed"})
    } 
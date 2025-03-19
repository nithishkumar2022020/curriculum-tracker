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
        # For GET /curriculum, just return the curriculum data
        return handle_get_curriculum()

    # Handle PUT requests
    if event["httpMethod"] == "PUT":
        try:
            data = json.loads(event["body"])
            path = event.get("path", "").strip("/")
            path_parts = path.split("/")
            
            # Extract IDs from the path
            if len(path_parts) >= 4 and path_parts[-4] == "module":
                module_id = int(path_parts[-3])
                topic_id = int(path_parts[-1])
                
                if "subtopic" in path_parts:
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
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

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

@app.route('/api/curriculum', methods=['GET'])
def get_curriculum():
    return jsonify(curriculum_data)

@app.route('/api/curriculum/module/<int:module_id>/topic/<int:topic_id>', methods=['PUT'])
def update_topic_status(module_id, topic_id):
    data = request.get_json()
    status = data.get('status')
    
    if status not in ["not_started", "in_progress", "completed"]:
        return jsonify({"error": "Invalid status value"}), 400
    
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
                    
                    return jsonify({"message": "Status updated successfully"})
    
    if not topic_found:
        return jsonify({"error": "Topic not found"}), 404
    
    return jsonify({"error": "Internal server error"}), 500

@app.route('/api/curriculum/module/<int:module_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>', methods=['PUT'])
def update_subtopic_status(module_id, topic_id, subtopic_id):
    data = request.get_json()
    status = data.get('status')
    
    if status not in ["not_started", "in_progress", "completed"]:
        return jsonify({"error": "Invalid status value"}), 400
    
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
                            
                            return jsonify({"message": "Status updated successfully"})
    
    if not subtopic_found:
        return jsonify({"error": "Subtopic not found"}), 404
    
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 
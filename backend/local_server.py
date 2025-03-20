from flask import Flask, request
from flask_cors import CORS
from netlify.functions.api import handler
import json

app = Flask(__name__)
CORS(app)

@app.route('/.netlify/functions/api/curriculum', methods=['GET'])
@app.route('/api/curriculum', methods=['GET'])
def get_curriculum():
    event = {
        "httpMethod": "GET",
        "path": "/api/curriculum"
    }
    response = handler(event, None)
    return response["body"], response["statusCode"], response["headers"]

@app.route('/api/curriculum/module/<int:module_id>/topic/<int:topic_id>/status', methods=['PUT', 'OPTIONS'])
def update_topic(module_id, topic_id):
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'PUT, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    
    status = request.args.get('status')
    event = {
        "httpMethod": "PUT",
        "path": f"/api/curriculum/module/{module_id}/topic/{topic_id}",
        "body": json.dumps({"status": status})
    }
    response = handler(event, None)
    return response["body"], response["statusCode"], response["headers"]

@app.route('/api/curriculum/module/<int:module_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/status', methods=['PUT', 'OPTIONS'])
def update_subtopic(module_id, topic_id, subtopic_id):
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'PUT, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    
    status = request.args.get('status')
    event = {
        "httpMethod": "PUT",
        "path": f"/api/curriculum/module/{module_id}/topic/{topic_id}/subtopic/{subtopic_id}",
        "body": json.dumps({"status": status})
    }
    response = handler(event, None)
    return response["body"], response["statusCode"], response["headers"]

if __name__ == '__main__':
    app.run(debug=True, port=8000) 
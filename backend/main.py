import os
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import logging
from enum import Enum
import json
from curriculum_data import get_curriculum_data, find_subtopic

# Setup logging with more detailed format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Full-Stack Development Progress Tracker")

# Get CORS origins from environment variable or use default
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3002")
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")
NETLIFY_URL = os.getenv("NETLIFY_URL", "")
GITHUB_PAGES_URL = os.getenv("GITHUB_PAGES_URL", "https://nithishkumar2022020.github.io")

logger.debug(f"FRONTEND_URL: {FRONTEND_URL}")
logger.debug(f"RENDER_EXTERNAL_URL: {RENDER_EXTERNAL_URL}")
logger.debug(f"NETLIFY_URL: {NETLIFY_URL}")
logger.debug(f"GITHUB_PAGES_URL: {GITHUB_PAGES_URL}")

# Define allowed origins
allowed_origins = [
    FRONTEND_URL,
    f"{GITHUB_PAGES_URL}",
    f"{GITHUB_PAGES_URL}/curriculum-tracker",
    f"{GITHUB_PAGES_URL}/curriculum-tracker/",
    "https://curriculum-tracker-frontend.onrender.com",
    "https://curriculum-tracker-frontend.onrender.com/",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "https://curriculum-tracker.netlify.app",
    "https://curriculum-tracker-app.netlify.app",
    "https://curriculum-tracker-new-frontend.onrender.com",
    "https://curriculum-tracker-new-frontend.onrender.com/"
]

# Add Render URLs if available
if RENDER_EXTERNAL_URL:
    allowed_origins.append(RENDER_EXTERNAL_URL)
    # Also allow the Render frontend URL
    if "backend" in RENDER_EXTERNAL_URL:
        frontend_url = RENDER_EXTERNAL_URL.replace("backend", "frontend")
        allowed_origins.append(frontend_url)
        allowed_origins.append(frontend_url + "/")

# Add Netlify URL if it exists
if NETLIFY_URL:
    allowed_origins.append(NETLIFY_URL)

logger.debug(f"Allowed origins: {allowed_origins}")

# Enable CORS with more specific settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
    expose_headers=["*"],
    max_age=3600,  # Cache preflight requests for 1 hour
)

# Add error handling middleware
@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    try:
        logger.debug(f"Request path: {request.url.path}")
        logger.debug(f"Request method: {request.method}")
        logger.debug(f"Request headers: {request.headers}")
        
        response = await call_next(request)
        logger.debug(f"Response status: {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"Error handling request: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": str(e)}
        )

# Data Models
class Subtopic(BaseModel):
    id: int
    name: str
    description: str
    duration: str
    status: str = "not_started"  # not_started, in_progress, completed
    completed_date: Optional[datetime] = None

class Topic(BaseModel):
    id: int
    name: str
    description: str
    duration: str
    status: str = "not_started"  # not_started, in_progress, completed
    completed_date: Optional[datetime] = None
    subtopics: List[Subtopic] = []

class Module(BaseModel):
    id: int
    name: str
    description: str
    duration: str
    topics: List[Topic]
    status: str = "not_started"
    progress: float = 0.0

class Curriculum(BaseModel):
    id: int
    name: str
    description: str
    modules: List[Module]
    total_progress: float = 0.0

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Welcome to Full-Stack Development Progress Tracker API"}

@app.get("/curriculum")
async def get_curriculum():
    return get_curriculum_data()

@app.put("/curriculum/module/{module_id}/topic/{topic_id}/subtopic/{subtopic_id}/status")
async def update_subtopic_status(module_id: int, topic_id: int, subtopic_id: int, status: str):
    logger.debug(f"Updating subtopic status: module={module_id}, topic={topic_id}, subtopic={subtopic_id}, status={status}")
    
    # Validate status
    if status not in ["not_started", "in_progress", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status value")
    
    # Find the subtopic
    subtopic = find_subtopic(module_id, topic_id, subtopic_id)
    if not subtopic:
        logger.error(f"Subtopic not found: module={module_id}, topic={topic_id}, subtopic={subtopic_id}")
        raise HTTPException(status_code=404, detail="Subtopic not found")
    
    # Update status
    subtopic["status"] = status
    if status == "completed":
        subtopic["completed_date"] = datetime.now()
    
    # Calculate progress
    curriculum = get_curriculum_data()
    total_subtopics = sum(len(t["subtopics"]) for m in curriculum["modules"] for t in m["topics"])
    completed_subtopics = sum(1 for m in curriculum["modules"] for t in m["topics"] for s in t["subtopics"] if s["status"] == "completed")
    curriculum["total_progress"] = (completed_subtopics / total_subtopics) * 100
    
    # Update module progress
    for module in curriculum["modules"]:
        module_subtopics = sum(len(t["subtopics"]) for t in module["topics"])
        module_completed = sum(1 for t in module["topics"] for s in t["subtopics"] if s["status"] == "completed")
        module["progress"] = (module_completed / module_subtopics) * 100 if module_subtopics > 0 else 0
    
    return curriculum

@app.get("/curriculum/progress")
async def get_progress():
    curriculum = get_curriculum_data()
    total_subtopics = sum(len(t["subtopics"]) for m in curriculum["modules"] for t in m["topics"])
    completed_subtopics = sum(1 for m in curriculum["modules"] for t in m["topics"] for s in t["subtopics"] if s["status"] == "completed")
    return {
        "total_progress": (completed_subtopics / total_subtopics) * 100 if total_subtopics > 0 else 0,
        "completed_subtopics": completed_subtopics,
        "total_subtopics": total_subtopics
    } 
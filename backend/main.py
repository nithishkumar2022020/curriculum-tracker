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

# Setup logging with more detailed format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Full-Stack Development Progress Tracker")

# Get CORS origins from environment variable or use default
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")
NETLIFY_URL = os.environ.get("NETLIFY_URL", "")
GITHUB_PAGES_URL = "https://nithishkumar2022020.github.io"

logger.debug(f"FRONTEND_URL: {FRONTEND_URL}")
logger.debug(f"RENDER_EXTERNAL_URL: {RENDER_EXTERNAL_URL}")
logger.debug(f"NETLIFY_URL: {NETLIFY_URL}")
logger.debug(f"GITHUB_PAGES_URL: {GITHUB_PAGES_URL}")

# If we're on Render, add the Render external URL to allowed origins
allowed_origins = [
    FRONTEND_URL,
    GITHUB_PAGES_URL,
    "https://nithishkumar2022020.github.io/curriculum-tracker",
    "https://nithishkumar2022020.github.io/curriculum-tracker/",
    "https://curriculum-tracker-frontend.onrender.com",
    "https://curriculum-tracker-frontend.onrender.com/",
    "http://localhost:3000",
    "http://localhost:3001"
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

# Add common Netlify deployment URLs
allowed_origins.extend([
    "https://curriculum-tracker.netlify.app",
    "https://curriculum-tracker-app.netlify.app",
])

logger.debug(f"Allowed origins: {allowed_origins}")

# Enable CORS with more specific settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
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
                            "description": "Function definitions, modules, packages, error handling",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 103,
                            "name": "Object-Oriented Programming",
                            "description": "Classes, inheritance, polymorphism, encapsulation",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 104,
                            "name": "Testing & Debugging",
                            "description": "Unit testing with pytest, debugging techniques",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 105,
                            "name": "REST API Basics",
                            "description": "Introduction to REST API design, FastAPI/Flask basics",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 106,
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
                            "id": 201,
                            "name": "SQL Fundamentals",
                            "description": "Queries, joins, normalization, indexing",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 202,
                            "name": "PostgreSQL",
                            "description": "Setup, schema design, migrations",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 203,
                            "name": "ORM & Database Design",
                            "description": "Django ORM/SQLAlchemy, database interactions",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 204,
                            "name": "MongoDB Basics",
                            "description": "CRUD operations, aggregation pipelines",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 205,
                            "name": "Library Management Project",
                            "description": "Build a system using both SQL and NoSQL",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "Production-Grade APIs (Weeks 6-8)",
                    "description": "Advanced API development, authentication, and deployment",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 301,
                            "name": "Advanced API Frameworks",
                            "description": "Django REST Framework/Flask-RESTx, best practices",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 302,
                            "name": "Authentication & Security",
                            "description": "JWT, OAuth2, rate limiting",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 303,
                            "name": "API Documentation",
                            "description": "OpenAPI/Swagger, API versioning",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 304,
                            "name": "Docker & Containerization",
                            "description": "Container setup, Docker Compose, deployment",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 305,
                            "name": "Task Management API Project",
                            "description": "Build a production-ready API with tests",
                            "duration": "7 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 2,
            "name": "Modern Frontend Development",
            "description": "Master modern frontend technologies and frameworks",
            "duration": "8 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 1,
                    "name": "Core Web Technologies",
                    "description": "Master HTML5, CSS3, and modern JavaScript fundamentals",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "HTML5 & Accessibility",
                            "description": "Learn semantic HTML5, ARIA roles, and responsive images",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "CSS Fundamentals",
                            "description": "Master CSS Grid, Flexbox, animations, and transitions",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Modern JavaScript",
                            "description": "ES6+ features, DOM manipulation, and Fetch API",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Recipe Browser Project",
                            "description": "Build an interactive recipe browser with search and filtering",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "React & TypeScript",
                    "description": "Build modern web applications with React and TypeScript",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "React Fundamentals",
                            "description": "Components, props, state, and hooks (useState, useEffect)",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "Advanced React",
                            "description": "Context, reducers, custom hooks, and TypeScript integration",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "State Management",
                            "description": "React Query, form handling with Formik, and validation",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Budget Tracker Project",
                            "description": "Create a budget tracking app with local storage",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "Full-Stack Frameworks",
                    "description": "Build production-ready applications with Next.js",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "Next.js Fundamentals",
                            "description": "App Router, SSR, ISG, and API routes",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "Authentication & Middleware",
                            "description": "Auth.js integration and protected routes",
                            "duration": "1 week",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Portfolio Site Project",
                            "description": "Build a portfolio site with CMS integration",
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
            "name": "Full-Stack Integration",
            "description": "6 weeks of full-stack integration and deployment",
            "duration": "6 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 1,
                    "name": "API Integration",
                    "description": "Connecting frontend with backend, error handling, and data flow",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "Backend-Frontend Communication",
                            "description": "RESTful API integration, data fetching patterns, Axios/Fetch",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "Error Handling & Validation",
                            "description": "Client/server validation, error boundaries, graceful degradation",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "State Management",
                            "description": "Context API, Redux Toolkit, server state with React Query",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "E-Commerce API Integration Project",
                            "description": "Build a product catalog with cart and checkout functionality",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Authentication & Authorization",
                    "description": "Implementing secure user authentication and role-based access",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "JWT Authentication",
                            "description": "Token-based auth, refresh tokens, secure storage",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "OAuth & Social Login",
                            "description": "Implementing OAuth 2.0, Google/GitHub integration",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Role-Based Access Control",
                            "description": "User roles, permissions, protected routes",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Secure Dashboard Project",
                            "description": "Build a multi-user dashboard with role-based permissions",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "Deployment & DevOps",
                    "description": "Cloud deployment, CI/CD pipelines, and monitoring",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "Cloud Services",
                            "description": "AWS/GCP basics, virtual machines, managed services",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "CI/CD Pipelines",
                            "description": "GitHub Actions, automated testing, deployment workflows",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Container Orchestration",
                            "description": "Docker Compose, Kubernetes basics, scaling applications",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Monitoring & Logging",
                            "description": "Application monitoring, error tracking, performance analysis",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 5,
                            "name": "Full-Stack SaaS Project",
                            "description": "Deploy a complete SaaS application with CI/CD and monitoring",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 4,
            "name": "ML & Cloud-Native Development",
            "description": "Build and deploy ML models and cloud-native applications",
            "duration": "6 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 1,
                    "name": "ML Engineering",
                    "description": "Machine learning fundamentals, model training, and deployment",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "Data Manipulation with Pandas",
                            "description": "Cleaning, transforming, and analyzing datasets",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "Scikit-learn Pipelines",
                            "description": "Building machine learning workflows for classification and regression",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Model Deployment with FastAPI",
                            "description": "Deploying ML models as REST APIs",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "ONNX Runtime Optimization",
                            "description": "Model optimization and cross-platform compatibility",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 5,
                            "name": "Model Monitoring",
                            "description": "Monitoring performance with Prometheus and Grafana",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 6,
                            "name": "Sentiment Analysis Project",
                            "description": "Build a sentiment analysis API with React dashboard",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Cloud Architecture",
                    "description": "AWS services, serverless computing, and infrastructure as code",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "AWS S3 for Object Storage",
                            "description": "Uploading, retrieving, and managing files in the cloud",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "AWS Lambda for Serverless",
                            "description": "Writing and deploying serverless functions",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Terraform Basics",
                            "description": "Infrastructure as Code for automating cloud provisioning",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Serverless API Development",
                            "description": "Integrating API Gateway with Lambda functions",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 5,
                            "name": "End-to-End Cloud Pipelines",
                            "description": "Building automated cloud-native pipelines",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 6,
                            "name": "Image Processing Pipeline Project",
                            "description": "Create a serverless image processing system on AWS",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 5,
            "name": "Advanced Specialization",
            "description": "Master advanced concepts and build production-ready systems",
            "duration": "8 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 1,
                    "name": "Microservices Architecture",
                    "description": "Design and implement scalable microservices systems",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "Domain-Driven Design",
                            "description": "Identifying bounded contexts and microservice boundaries",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "gRPC Communication",
                            "description": "High-performance inter-service communication",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Event-Driven Architecture",
                            "description": "RabbitMQ/Kafka for message streaming and event sourcing",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Service Discovery & Load Balancing",
                            "description": "Managing service registration and traffic distribution",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 5,
                            "name": "Distributed Tracing",
                            "description": "Monitoring service interactions with Jaeger/Zipkin",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 6,
                            "name": "E-Commerce Services Project",
                            "description": "Build cart and inventory microservices with gRPC and event streaming",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Performance Mastery",
                    "description": "Optimize applications for high performance and scalability",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "Redis Caching Strategies",
                            "description": "Cache invalidation, TTL, and data partitioning",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "CDN Integration",
                            "description": "Setting up CDNs for static assets and content delivery",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Database Scaling",
                            "description": "Sharding and replication for horizontal scaling",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Query Optimization",
                            "description": "Indexing, query rewriting, and performance profiling",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 5,
                            "name": "Load Testing",
                            "description": "Performance testing and bottleneck identification",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 6,
                            "name": "High-Traffic News API Project",
                            "description": "Build a scalable news API with caching and CDN",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "Capstone Project",
                    "description": "Build a production-ready social platform with advanced features",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1,
                            "name": "Real-time Notifications",
                            "description": "Implement WebSockets and server-sent events",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 2,
                            "name": "AI Content Recommendations",
                            "description": "Build recommendation engine with collaborative filtering",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 3,
                            "name": "Kubernetes Deployment",
                            "description": "Container orchestration and cluster management",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 4,
                            "name": "Payment Integration",
                            "description": "Integrate Stripe/PayPal for payment processing",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 5,
                            "name": "Project Documentation",
                            "description": "Comprehensive documentation and presentation",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 6,
                            "name": "Social Platform Project",
                            "description": "Complete social platform with all advanced features",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        }
    ]
}

# API Endpoints
@app.get("/")
async def root():
    logger.debug("Root endpoint called")
    return {"message": "Welcome to Full-Stack Development Progress Tracker API"}

@app.get("/curriculum")
async def get_curriculum():
    logger.debug("Curriculum endpoint called")
    return curriculum_data

@app.put("/curriculum/module/{module_id}/topic/{topic_id}/status")
async def update_topic_status(module_id: int, topic_id: int, status: str):
    logging.info(f"Updating status for module {module_id}, topic {topic_id} to {status}")
    if status not in ["not_started", "in_progress", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status value")
        
    topic_found = False
    for module in curriculum_data["modules"]:
        if module["id"] == module_id:
            for topic in module["topics"]:
                if topic["id"] == topic_id:
                    topic_found = True
                    topic["status"] = status
                    if status == "completed":
                        topic["completed_date"] = datetime.now()
                        # Mark all subtopics as completed
                        for subtopic in topic.get("subtopics", []):
                            subtopic["status"] = "completed"
                            subtopic["completed_date"] = datetime.now()
                    elif status == "not_started":
                        topic["completed_date"] = None
                        # Mark all subtopics as not started
                        for subtopic in topic.get("subtopics", []):
                            subtopic["status"] = "not_started"
                            subtopic["completed_date"] = None
                    
                    # Update topic progress based on subtopics
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
                    
                    return {"message": "Status updated successfully"}
    
    if not topic_found:
        logging.error(f"Topic {topic_id} not found in module {module_id}")
        raise HTTPException(status_code=404, detail="Topic not found")
    raise HTTPException(status_code=500, detail="Internal server error")

@app.put("/curriculum/module/{module_id}/topic/{topic_id}/subtopic/{subtopic_id}/status")
async def update_subtopic_status(module_id: int, topic_id: int, subtopic_id: int, status: str):
    logging.info(f"Updating status for module {module_id}, topic {topic_id}, subtopic {subtopic_id} to {status}")
    if status not in ["not_started", "in_progress", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status value")
    
    # For Module 1, handle both prefixed and non-prefixed subtopic IDs
    actual_subtopic_id = subtopic_id
    if module_id == 1:
        # If the subtopic ID is already prefixed (e.g., 201), use it as is
        # If it's not prefixed (e.g., 1), prefix it with the topic ID
        if len(str(subtopic_id)) <= 2:
            actual_subtopic_id = int(str(topic_id) + str(subtopic_id).zfill(2))
    
    subtopic_found = False
    for module in curriculum_data["modules"]:
        if module["id"] == module_id:
            for topic in module["topics"]:
                if topic["id"] == topic_id:
                    for subtopic in topic.get("subtopics", []):
                        if subtopic["id"] == actual_subtopic_id:
                            subtopic_found = True
                            subtopic["status"] = status
                            if status == "completed":
                                subtopic["completed_date"] = datetime.now()
                            elif status == "not_started":
                                subtopic["completed_date"] = None
                            
                            # Update topic progress based on subtopics
                            total_subtopics = len(topic["subtopics"])
                            completed_subtopics = sum(1 for s in topic["subtopics"] if s["status"] == "completed")
                            topic["progress"] = (completed_subtopics / total_subtopics) * 100
                            
                            # Update topic status based on subtopics
                            if all(s["status"] == "completed" for s in topic["subtopics"]):
                                topic["status"] = "completed"
                                topic["completed_date"] = datetime.now()
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
                            
                            return {"message": "Status updated successfully"}
    
    if not subtopic_found:
        logging.error(f"Subtopic {actual_subtopic_id} not found in topic {topic_id} of module {module_id}")
        raise HTTPException(status_code=404, detail="Subtopic not found")
    raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/curriculum/progress")
async def get_progress():
    return {
        "total_progress": curriculum_data["total_progress"],
        "modules": [
            {
                "id": module["id"],
                "name": module["name"],
                "progress": module["progress"]
            }
            for module in curriculum_data["modules"]
        ]
    } 
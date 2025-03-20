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
            "description": "8 weeks of comprehensive Python backend development",
            "duration": "8 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 1,
                    "name": "Python Fundamentals (Weeks 1-2)",
                    "description": "Core Python concepts and initial API development",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 101,
                            "name": "Core Python Concepts",
                            "description": "Python syntax, data types, control flow, functions, modules",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 102,
                            "name": "Object-Oriented Programming",
                            "description": "Classes, inheritance, polymorphism, encapsulation",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 103,
                            "name": "Testing & Debugging",
                            "description": "Unit testing with pytest, debugging techniques",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 104,
                            "name": "Weather API Project",
                            "description": "Build a weather API with caching using public APIs",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Database Engineering (Weeks 3-5)",
                    "description": "SQL, NoSQL, and database integration",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 201,
                            "name": "SQL Fundamentals",
                            "description": "Queries, joins, normalization, indexing with PostgreSQL",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 202,
                            "name": "ORM Integration",
                            "description": "Django ORM/SQLAlchemy for database operations",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 203,
                            "name": "MongoDB & NoSQL",
                            "description": "CRUD operations, aggregation pipelines in MongoDB",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 204,
                            "name": "Library Management System",
                            "description": "Build a dual-database library system (SQL + NoSQL)",
                            "duration": "7 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "Production-Grade APIs (Weeks 6-8)",
                    "description": "Advanced API development and deployment",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 301,
                            "name": "Advanced API Frameworks",
                            "description": "Django REST Framework or Flask-RESTx implementation",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 302,
                            "name": "Authentication & Security",
                            "description": "JWT, OAuth2, rate limiting implementation",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 303,
                            "name": "API Documentation",
                            "description": "OpenAPI/Swagger documentation and testing",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 304,
                            "name": "Containerization",
                            "description": "Docker, Docker Compose for app and database",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 305,
                            "name": "Task Management API Project",
                            "description": "Build and deploy a full-featured task management API",
                            "duration": "5 days",
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
            "description": "8 weeks of comprehensive frontend development",
            "duration": "8 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 4,
                    "name": "Core Web Technologies (Weeks 1-3)",
                    "description": "HTML5, CSS3, and modern JavaScript fundamentals",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 401,
                            "name": "HTML5 & Accessibility",
                            "description": "Semantic HTML, ARIA roles, responsive images",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 402,
                            "name": "Modern CSS",
                            "description": "Grid, Flexbox, animations, SCSS, Tailwind CSS",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 403,
                            "name": "JavaScript ES6+",
                            "description": "Modern JS features, DOM manipulation, Fetch API",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 404,
                            "name": "Recipe Browser Project",
                            "description": "Build an interactive recipe browser with API integration",
                            "duration": "7 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 5,
                    "name": "React & TypeScript (Weeks 4-6)",
                    "description": "Modern React development with TypeScript",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 501,
                            "name": "React Fundamentals",
                            "description": "Components, props, state, hooks (useState, useEffect)",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 502,
                            "name": "Advanced React",
                            "description": "Custom hooks, Context API, React Query",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 503,
                            "name": "TypeScript Integration",
                            "description": "Type annotations, interfaces, props typing",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 504,
                            "name": "Form Handling",
                            "description": "Formik, Yup validation, controlled components",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 505,
                            "name": "Budget Tracker Project",
                            "description": "Build a budget tracker with TypeScript and local storage",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 6,
                    "name": "Full-Stack Frameworks (Weeks 7-8)",
                    "description": "Next.js and modern full-stack development",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 601,
                            "name": "Next.js Fundamentals",
                            "description": "App Router, SSR, ISG, API routes",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 602,
                            "name": "Authentication & Middleware",
                            "description": "Auth.js integration, protected routes",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 603,
                            "name": "CMS Integration",
                            "description": "Headless CMS setup (Strapi/Contentful)",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 604,
                            "name": "Portfolio Site Project",
                            "description": "Build a portfolio with blog and CMS integration",
                            "duration": "4 days",
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
            "description": "6 weeks of comprehensive full-stack development",
            "duration": "6 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 7,
                    "name": "System Design (Weeks 1-2)",
                    "description": "Modern API design and real-time communication",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 701,
                            "name": "API Architecture",
                            "description": "REST vs GraphQL, hybrid approaches, Apollo integration",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 702,
                            "name": "Real-Time Communication",
                            "description": "WebSockets with Socket.IO, Redis pub/sub",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 703,
                            "name": "File Management",
                            "description": "S3 presigned URLs, large file handling",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 704,
                            "name": "Real-Time Polling Project",
                            "description": "Build a polling app with live updates using WebSocket and Redis",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 8,
                    "name": "DevOps Foundations (Weeks 3-4)",
                    "description": "Containerization and deployment automation",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 801,
                            "name": "Containerization",
                            "description": "Docker Compose, multi-container applications",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 802,
                            "name": "Load Balancing",
                            "description": "NGINX setup, SSL termination, reverse proxy",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 803,
                            "name": "CI/CD & Quality",
                            "description": "GitHub Actions, SonarCloud integration",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 804,
                            "name": "Task API Deployment",
                            "description": "Deploy containerized Task API to AWS EC2/ECS",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 9,
                    "name": "Security & Testing (Weeks 5-6)",
                    "description": "Application security and comprehensive testing",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 901,
                            "name": "Security Implementation",
                            "description": "OWASP Top 10, CSP headers, XSS protection",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 902,
                            "name": "Testing Strategy",
                            "description": "Unit testing with Jest/RTL, E2E with Playwright",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 903,
                            "name": "Performance Testing",
                            "description": "Load testing with k6, traffic simulation",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 904,
                            "name": "Secure Chat Project",
                            "description": "Build a secure real-time chat app with testing",
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
            "description": "6 weeks of machine learning and cloud architecture",
            "duration": "6 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 10,
                    "name": "ML Engineering (Weeks 1-3)",
                    "description": "Machine learning model development and deployment",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1001,
                            "name": "Data Processing",
                            "description": "Data manipulation with Pandas, cleaning and analysis",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1002,
                            "name": "Model Development",
                            "description": "Scikit-learn pipelines, training, and evaluation",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1003,
                            "name": "Model Optimization",
                            "description": "ONNX runtime for model optimization",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1004,
                            "name": "Model Monitoring",
                            "description": "Prometheus and Grafana for performance metrics",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1005,
                            "name": "Sentiment Analysis Project",
                            "description": "Build a sentiment analysis API with React dashboard",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 11,
                    "name": "Cloud Architecture (Weeks 4-6)",
                    "description": "AWS services and infrastructure automation",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1101,
                            "name": "AWS Storage",
                            "description": "S3 for object storage and file management",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1102,
                            "name": "Serverless Computing",
                            "description": "AWS Lambda functions and API Gateway",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1103,
                            "name": "Infrastructure as Code",
                            "description": "Terraform for cloud resource provisioning",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1104,
                            "name": "Image Processing Pipeline",
                            "description": "Build end-to-end serverless image processing pipeline",
                            "duration": "8 days",
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
            "description": "8 weeks of advanced system design and performance optimization",
            "duration": "8 weeks",
            "progress": 0.0,
            "status": "not_started",
            "topics": [
                {
                    "id": 12,
                    "name": "Microservices (Weeks 1-3)",
                    "description": "Advanced microservices architecture and implementation",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1201,
                            "name": "Domain-Driven Design",
                            "description": "Bounded contexts, microservice boundaries, DDD principles",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1202,
                            "name": "Service Communication",
                            "description": "gRPC implementation, service discovery, load balancing",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1203,
                            "name": "Event-Driven Architecture",
                            "description": "RabbitMQ/Kafka setup, event sourcing patterns",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1204,
                            "name": "Distributed Tracing",
                            "description": "Jaeger/Zipkin implementation for service monitoring",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1205,
                            "name": "E-Commerce Services Project",
                            "description": "Build cart and inventory microservices with event streaming",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 13,
                    "name": "Performance Mastery (Weeks 4-6)",
                    "description": "Advanced caching and performance optimization",
                    "duration": "3 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1301,
                            "name": "Caching Strategies",
                            "description": "Redis implementation, cache invalidation, TTL",
                            "duration": "4 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1302,
                            "name": "Content Delivery",
                            "description": "CDN setup, static asset optimization",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1303,
                            "name": "Database Optimization",
                            "description": "Sharding, replication, query optimization",
                            "duration": "5 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1304,
                            "name": "Load Testing",
                            "description": "Performance testing, bottleneck identification",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1305,
                            "name": "News API Project",
                            "description": "Build high-traffic news API with caching and optimization",
                            "duration": "6 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                },
                {
                    "id": 14,
                    "name": "Capstone Project (Weeks 7-8)",
                    "description": "Final project combining advanced technologies",
                    "duration": "2 weeks",
                    "status": "not_started",
                    "completed_date": None,
                    "subtopics": [
                        {
                            "id": 1401,
                            "name": "Real-Time Features",
                            "description": "WebSocket/SSE implementation for notifications",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1402,
                            "name": "AI Integration",
                            "description": "Recommendation engine with collaborative filtering",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1403,
                            "name": "Kubernetes Deployment",
                            "description": "Container orchestration and scaling",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1404,
                            "name": "Payment Integration",
                            "description": "Stripe/PayPal gateway implementation",
                            "duration": "2 days",
                            "status": "not_started",
                            "completed_date": None
                        },
                        {
                            "id": 1405,
                            "name": "Social Platform Project",
                            "description": "Complete social platform with all features integrated",
                            "duration": "3 days",
                            "status": "not_started",
                            "completed_date": None
                        }
                    ]
                }
            ]
        },
        {
            "id": 6,
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
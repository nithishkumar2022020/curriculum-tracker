# Curriculum Progress Tracker

A full-stack web application to track progress through a software development curriculum. Built with FastAPI (backend) and Next.js (frontend).

## Features

- Track progress through multiple modules and topics
- Granular tracking of subtopics
- Dark theme UI
- Interactive progress bars
- Responsive design

## Tech Stack

- **Backend**: FastAPI, Python
- **Frontend**: Next.js, TypeScript, TailwindCSS
- **Deployment**: Render

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm/yarn

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Usage

- Access the frontend at: http://localhost:3000
- API endpoint: http://localhost:8000

## Deployment

This application is configured for deployment on Render.com with the provided configuration files:
- `backend/Procfile` and `frontend/Procfile` for service configuration
- Environment variables control the API connection between services 
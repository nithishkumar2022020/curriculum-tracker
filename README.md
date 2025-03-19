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

## Deployment to Render (Free Tier)

### Backend Deployment

1. Go to [Render.com](https://render.com/) and create an account
2. Click "New" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: `curriculum-tracker-backend`
   - Root Directory: `backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add the following environment variable:
   - `FRONTEND_URL` = `https://curriculum-tracker-frontend.onrender.com`
6. Select the free plan and click "Create Web Service"

### Frontend Deployment

1. Go to Render.com and click "New" > "Web Service"
2. Connect to the same GitHub repository
3. Configure the service:
   - Name: `curriculum-tracker-frontend`
   - Root Directory: `frontend`
   - Environment: `Node`
   - Build Command: `npm install && npm run build`
   - Start Command: `npm start`
4. Add the following environment variable:
   - `NEXT_PUBLIC_API_URL` = `https://curriculum-tracker-backend.onrender.com`
5. Select the free plan and click "Create Web Service"

> **Note**: The free tier of Render will spin down after 15 minutes of inactivity. The first request after inactivity will take longer as the service spins up again. 
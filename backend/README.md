# Curriculum Tracker Backend

FastAPI backend for the Curriculum Progress Tracker application.

## Local Development

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
# venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Free Hosting Options

### Option 1: PythonAnywhere (Recommended)

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com/)
2. Go to the "Web" tab and choose "Add a new web app"
3. Select "Manual configuration" and choose Python 3.9
4. Set up the virtual environment:
   ```bash
   mkvirtualenv --python=python3.9 myenv
   pip install -r requirements.txt
   ```
5. Configure the WSGI file to point to your FastAPI app
6. Set the following environment variables:
   - `FRONTEND_URL` - URL of your Netlify frontend
7. Add CORS configuration to allow requests from your frontend

### Option 2: Render Free Tier

1. Create an account at [Render](https://render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: `curriculum-tracker-api`
   - Root Directory: `backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add the environment variable:
   - `FRONTEND_URL` = URL of your Netlify frontend
6. Select the free plan and click "Create Web Service"

### Option 3: Railway

1. Create an account at [Railway](https://railway.app/)
2. Create a new project from GitHub
3. Select your repository
4. Set the root directory to `/backend`
5. Add the environment variable:
   - `FRONTEND_URL` = URL of your Netlify frontend
6. Deploy the service

## Environment Variables

The following environment variables need to be set:

- `FRONTEND_URL` - URL of the frontend (e.g., your Netlify site) 
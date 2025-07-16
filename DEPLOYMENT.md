# Deployment Guide

This guide will help you deploy the Curriculum Progress Tracker using GitHub Actions.

## Prerequisites

1. **GitHub Repository**: Your code should be in a GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com) (free tier available)
3. **GitHub Pages**: Enable GitHub Pages in your repository settings

## Deployment Architecture

- **Frontend**: Deployed to GitHub Pages (Static Site)
- **Backend**: Deployed to Render (Free tier with auto-sleep)

## Step-by-Step Deployment

### 1. Setup GitHub Repository

1. Push your code to GitHub:
```bash
git add .
git commit -m "Initial commit with deployment setup"
git push origin main
```

### 2. Deploy Backend to Render

1. Go to [render.com](https://render.com) and sign up/login
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `curriculum-tracker-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (with auto-sleep after 15 minutes of inactivity)

5. Add Environment Variables:
   - `PYTHON_VERSION`: `3.11.0`
   - `FRONTEND_URL`: `https://[your-username].github.io/curriculum-tracker`

6. Click "Create Web Service"
7. Note your backend URL (e.g., `https://curriculum-tracker-backend-xyz.onrender.com`)

### 3. Deploy Frontend to GitHub Pages

1. Go to your GitHub repository
2. Navigate to **Settings** → **Pages**
3. Under "Source", select **GitHub Actions**
4. The workflow will automatically deploy when you push to main branch

### 4. Update API Configuration

Update the backend URL in your repository:

1. Edit `frontend/src/app/api.ts` and update the fallback URL if needed
2. Update `.github/workflows/deploy-frontend.yml` with your actual backend URL
3. Commit and push changes

### 5. Enable GitHub Actions

1. Go to your repository → **Actions** tab
2. Enable workflows if prompted
3. The deployment will trigger automatically on push to main branch

## Environment Variables

### Backend (Render)
- `PYTHON_VERSION`: `3.11.0`
- `FRONTEND_URL`: Your GitHub Pages URL
- `PORT`: Automatically set by Render

### Frontend (GitHub Actions)
- `NEXT_PUBLIC_API_URL`: Your Render backend URL

## URLs After Deployment

- **Frontend**: `https://[your-username].github.io/curriculum-tracker`
- **Backend**: `https://[your-service-name].onrender.com`

## Troubleshooting

### Backend Issues
- Check Render logs in the dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify the start command is correct

### Frontend Issues
- Check GitHub Actions logs
- Ensure the build completes successfully
- Verify the API URL is correct

### CORS Issues
- The backend is configured to allow all origins for development
- For production, update the CORS settings in `backend/main.py`

## Free Tier Limitations

### Render (Backend)
- Service sleeps after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake up
- 750 hours/month free (enough for personal projects)

### GitHub Pages (Frontend)
- 1GB storage limit
- 100GB bandwidth/month
- Public repositories only (for free accounts)

## Monitoring

- **Backend**: Monitor via Render dashboard
- **Frontend**: Monitor via GitHub Actions
- **Uptime**: Consider using a service like UptimeRobot to ping your backend periodically

## Custom Domain (Optional)

1. **Frontend**: Configure custom domain in GitHub Pages settings
2. **Backend**: Upgrade to Render paid plan for custom domain support

## Security Notes

- API keys and secrets should be stored as GitHub Secrets
- Never commit sensitive information to the repository
- Consider implementing rate limiting for production use
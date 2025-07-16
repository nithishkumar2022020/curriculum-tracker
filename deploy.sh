#!/bin/bash

# Curriculum Progress Tracker - Deployment Script
# This script helps you deploy the application step by step

set -e

echo "🚀 Curriculum Progress Tracker - Deployment Setup"
echo "=================================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check if we're on main/master branch
BRANCH=$(git branch --show-current)
if [ "$BRANCH" != "main" ] && [ "$BRANCH" != "master" ]; then
    echo "⚠️  You're on branch '$BRANCH'. Consider switching to 'main' or 'master' for deployment."
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "✅ Git repository ready"

# Check if GitHub remote exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ No GitHub remote found. Please add your GitHub repository:"
    echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    exit 1
fi

GITHUB_URL=$(git remote get-url origin)
echo "✅ GitHub remote: $GITHUB_URL"

# Extract username and repo name from GitHub URL
if [[ $GITHUB_URL =~ github\.com[:/]([^/]+)/([^/]+)(\.git)?$ ]]; then
    USERNAME=${BASH_REMATCH[1]}
    REPO=${BASH_REMATCH[2]%.git}
    echo "📝 Detected: Username=$USERNAME, Repository=$REPO"
else
    echo "❌ Could not parse GitHub URL. Please check your remote URL."
    exit 1
fi

# Update README with correct GitHub Pages URL
GITHUB_PAGES_URL="https://$USERNAME.github.io/$REPO"
echo "🔗 Your GitHub Pages URL will be: $GITHUB_PAGES_URL"

# Update the deployment workflow with the correct backend URL
echo "📝 Please provide your Render backend URL (or press Enter to use default):"
read -p "Backend URL [https://curriculum-tracker-backend.onrender.com]: " BACKEND_URL
BACKEND_URL=${BACKEND_URL:-"https://curriculum-tracker-backend.onrender.com"}

# Update the frontend deployment workflow
sed -i.bak "s|NEXT_PUBLIC_API_URL: https://curriculum-tracker-new-backend.onrender.com|NEXT_PUBLIC_API_URL: $BACKEND_URL|g" .github/workflows/deploy-frontend.yml
sed -i.bak "s|NEXT_PUBLIC_API_URL: https://curriculum-tracker-new-backend.onrender.com|NEXT_PUBLIC_API_URL: $BACKEND_URL|g" .github/workflows/test-and-lint.yml

# Update README with correct demo URL
sed -i.bak "s|\[your-username\]\.github\.io/curriculum-tracker|$USERNAME.github.io/$REPO|g" README.md

# Clean up backup files
rm -f .github/workflows/deploy-frontend.yml.bak .github/workflows/test-and-lint.yml.bak README.md.bak

echo "✅ Configuration updated"

# Check if changes need to be committed
if ! git diff --quiet; then
    echo "📝 Committing configuration changes..."
    git add .
    git commit -m "Configure deployment for $USERNAME/$REPO"
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push origin $BRANCH

echo ""
echo "🎉 Deployment setup complete!"
echo ""
echo "Next steps:"
echo "1. 🔧 Deploy Backend to Render:"
echo "   - Go to https://render.com"
echo "   - Create new Web Service"
echo "   - Connect your GitHub repo: $GITHUB_URL"
echo "   - Root Directory: backend"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: uvicorn main:app --host 0.0.0.0 --port \$PORT"
echo "   - Add Environment Variable: FRONTEND_URL = $GITHUB_PAGES_URL"
echo ""
echo "2. 🌐 Enable GitHub Pages:"
echo "   - Go to $GITHUB_URL/settings/pages"
echo "   - Source: GitHub Actions"
echo "   - The frontend will deploy automatically"
echo ""
echo "3. 🔗 Your URLs:"
echo "   - Frontend: $GITHUB_PAGES_URL"
echo "   - Backend: $BACKEND_URL"
echo ""
echo "4. 📊 Monitor deployment:"
echo "   - GitHub Actions: $GITHUB_URL/actions"
echo "   - Render Dashboard: https://dashboard.render.com"
echo ""
echo "Happy coding! 🚀"
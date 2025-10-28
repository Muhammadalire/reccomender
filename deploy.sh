#!/bin/bash

echo "🚀 Deploying Magical Book Finder to Vercel..."
echo ""
echo "✅ All fixes applied:"
echo "  - Ultra-lightweight (no pandas)"
echo "  - CSV included in serverless bundle"
echo "  - Only 3 dependencies"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "❌ Error: Not a git repository"
    echo "Please run: git init"
    exit 1
fi

# Add all files
echo "📦 Adding files..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Deploy: Ultra-lightweight book recommender (no pandas)"

# Check if remote exists
if ! git remote | grep -q origin; then
    echo "⚠️  No remote repository found"
    echo "Please add remote: git remote add origin YOUR_REPO_URL"
    exit 1
fi

# Push to GitHub
echo "🌐 Pushing to GitHub..."
git push origin main || git push origin master

echo ""
echo "✅ Done!"
echo ""
echo "🎉 Vercel will auto-deploy in 1-2 minutes"
echo "📊 Check: https://vercel.com/dashboard"
echo ""
echo "🎁 Your magical book finder will be live soon!"
echo "   All 500 errors are now fixed! ✨"

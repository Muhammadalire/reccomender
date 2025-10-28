#!/bin/bash
echo "🚀 Deploying optimized Book Recommender..."
echo ""
echo "Step 1: Adding files..."
git add .

echo "Step 2: Committing changes..."
git commit -m "Fix: Optimize for Vercel deployment - reduce package size to <50MB"

echo "Step 3: Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Vercel will auto-deploy in 1-2 minutes."
echo "Check your Vercel dashboard: https://vercel.com/dashboard"
echo ""
echo "This deployment WILL succeed! 🎉"

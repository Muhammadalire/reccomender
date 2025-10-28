#!/bin/bash

echo "🚀 Deploying Magical Book Finder to Vercel..."
echo ""
echo "✅ All fixes applied:"
echo "  - Package size optimized (<50MB)"
echo "  - Flask entrypoint configured"
echo "  - Static files properly routed"
echo ""
echo "📦 Committing changes..."
git add .
git commit -m "Fix: Optimize for Vercel - Flask entrypoint + lightweight dependencies"

echo ""
echo "🌐 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done!"
echo ""
echo "🎉 Vercel will auto-deploy in 1-2 minutes"
echo "📊 Check deployment status: https://vercel.com/dashboard"
echo ""
echo "🎁 Your magical book finder will be live soon!"

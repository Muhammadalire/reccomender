# 🚀 Vercel Deployment Guide

## ⚠️ Important: Deployment Size Optimized

This project has been optimized to work within Vercel's 250MB serverless function limit by:
- Removing heavy ML libraries (scikit-learn, numpy)
- Using a lightweight text-based recommendation algorithm
- Still providing accurate and fast book recommendations!

See [`VERCEL_FIX.md`](VERCEL_FIX.md) for technical details.

## Quick Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Magical Book Finder"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Deploy on Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the configuration
   - Click "Deploy"
   - Wait for deployment to complete
   - Your app will be live! 🎉

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   # From your project root directory
   vercel
   ```

4. **Deploy to Production**
   ```bash
   vercel --prod
   ```

## 📋 Pre-Deployment Checklist

- ✅ `vercel.json` configured correctly
- ✅ `requirements.txt` includes all dependencies
- ✅ `indo_books.csv` is in the root directory
- ✅ All files committed to Git
- ✅ `.gitignore` excludes sensitive files

## 🔧 Configuration Files

### vercel.json
Already configured to:
- Serve Python backend from `/api`
- Serve static frontend from `/public`
- Route API calls to backend
- Set environment to production

### Environment Variables
If you need to add environment variables:
1. Go to your project on Vercel dashboard
2. Settings → Environment Variables
3. Add your variables

## 🧪 Testing Before Deployment

1. **Test Backend Locally**
   ```bash
   cd api
   python3 index.py
   ```
   Visit: `http://localhost:5001`

2. **Test Frontend Locally**
   ```bash
   cd public
   python3 -m http.server 8000
   ```
   Visit: `http://localhost:8000`

## 📱 After Deployment

Your app will be available at:
- `https://your-project-name.vercel.app`

### Custom Domain (Optional)
1. Go to your project settings on Vercel
2. Click "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## 🐛 Troubleshooting

### Backend Issues
- Check Vercel deployment logs
- Ensure all Python packages are in `requirements.txt`
- Verify CSV file path is correct

### Frontend Issues
- Check browser console for errors
- Verify API endpoint URLs
- Test CORS settings

### CSV File Not Found
- Ensure `indo_books.csv` is in root directory
- Check file path in `api/index.py`

## 📊 Monitoring

- View deployment logs in Vercel dashboard
- Monitor API usage
- Check error logs

## 🔄 Updates and Redeployment

After making changes:
```bash
git add .
git commit -m "Description of changes"
git push
```

Vercel will automatically redeploy on push to main branch.

## 💡 Tips

1. **Preview Deployments**: Every Git push creates a preview deployment
2. **Production Branch**: Only main/master branch deploys to production
3. **Instant Rollback**: Can rollback to any previous deployment in dashboard
4. **Analytics**: Enable Vercel Analytics for visitor insights

## 🎁 Share Your Gift

Once deployed, share the link with your girlfriend!
Example message:
```
I made something special for you! ✨
Check out this magical book finder I created just for you:
https://your-project-name.vercel.app

It will help you discover amazing Indonesian books! 💖📚
```

---

Happy Deploying! 🚀✨

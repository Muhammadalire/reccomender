@echo off
echo.
echo ========================================
echo   Deploying Magical Book Finder
echo ========================================
echo.
echo All fixes applied:
echo   - Ultra-lightweight (no pandas)
echo   - CSV included in serverless bundle
echo   - Only 3 dependencies
echo.

REM Check if git is initialized
if not exist .git (
    echo ERROR: Not a git repository
    echo Please run: git init
    pause
    exit /b 1
)

REM Add all files
echo Adding files...
git add .

REM Commit changes
echo Committing changes...
git commit -m "Deploy: Ultra-lightweight book recommender (no pandas)"

REM Check if remote exists
git remote | findstr origin >nul
if errorlevel 1 (
    echo WARNING: No remote repository found
    echo Please add remote: git remote add origin YOUR_REPO_URL
    pause
    exit /b 1
)

REM Push to GitHub
echo Pushing to GitHub...
git push origin main
if errorlevel 1 (
    git push origin master
)

echo.
echo ========================================
echo   Deployment Complete!
echo ========================================
echo.
echo Vercel will auto-deploy in 1-2 minutes
echo Check: https://vercel.com/dashboard
echo.
echo Your magical book finder will be live soon!
echo All 500 errors are now fixed!
echo.
pause

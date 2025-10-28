# 💻 Local Development Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser

## Setup Instructions

### 1. Install Dependencies

```bash
# Navigate to project directory
cd /path/to/reccomender

# Install Python packages
pip install -r requirements.txt
# or
python3 -m pip install -r requirements.txt
```

### 2. Run the Backend

```bash
# Start the Flask API server
cd api
python3 index.py
```

The backend will run on `http://localhost:5001`

You should see:
```
 * Running on http://127.0.0.1:5001
 * Debug mode: on
```

### 3. Run the Frontend

Open a new terminal window:

```bash
# Navigate to public directory
cd public

# Start a simple HTTP server
python3 -m http.server 8000
```

The frontend will be available at `http://localhost:8000`

### 4. Test the Application

Open your browser and go to:
```
http://localhost:8000
```

You should see the beautiful Disney-styled book finder! ✨

## Testing the API Endpoints

### Test Health Check
```bash
curl http://localhost:5001/
```

### Get All Genres
```bash
curl http://localhost:5001/api/genres
```

### Search Books
```bash
curl "http://localhost:5001/api/search?q=romance"
```

### Get Recommendations
```bash
curl -X POST http://localhost:5001/api/recommend \
  -H "Content-Type: application/json" \
  -d '{"title": "Hujan", "count": 5}'
```

### Get Random Books
```bash
curl http://localhost:5001/api/random?count=5
```

## Project Structure

```
reccomender/
├── api/
│   └── index.py              # Flask backend API
├── public/
│   ├── index.html           # Main HTML page
│   ├── styles.css           # Disney-styled CSS
│   └── script.js            # Frontend JavaScript
├── indo_books.csv           # Book database
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel config
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── README.md              # Main documentation
├── DEPLOYMENT.md          # Deployment guide
└── DEV.md                # This file
```

## Development Workflow

### Making Changes to Backend

1. Edit `api/index.py`
2. Save the file
3. Flask auto-reloads (in debug mode)
4. Test the changes in your browser

### Making Changes to Frontend

1. Edit HTML/CSS/JS files in `public/`
2. Save the file
3. Refresh your browser (Ctrl+R or Cmd+R)
4. See the changes immediately

## Common Issues & Solutions

### Port Already in Use

**Error**: `Address already in use: Port 5001`

**Solution**: 
```bash
# Find process using the port
lsof -ti:5001

# Kill the process
kill -9 $(lsof -ti:5001)

# Or use a different port
# Edit api/index.py and change the port number
```

### CSV File Not Found

**Error**: `FileNotFoundError: indo_books.csv`

**Solution**: 
- Ensure `indo_books.csv` is in the root directory
- Check the path in `api/index.py`

### CORS Issues

**Error**: `CORS policy: No 'Access-Control-Allow-Origin'`

**Solution**:
- Flask-CORS is already configured
- Make sure you're running both backend and frontend
- Check that API_BASE_URL in `script.js` is correct

### Python Package Errors

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install -r requirements.txt
```

## Useful Commands

### Check Python Version
```bash
python3 --version
```

### List Installed Packages
```bash
pip list
```

### Update Requirements
```bash
pip freeze > requirements.txt
```

### Check for Syntax Errors
```bash
python3 -m py_compile api/index.py
```

## Browser DevTools Tips

### Open DevTools
- Chrome/Edge: `F12` or `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac)
- Firefox: `F12` or `Ctrl+Shift+K` (Windows) / `Cmd+Option+K` (Mac)

### Useful Tabs
- **Console**: View JavaScript errors and logs
- **Network**: Monitor API requests
- **Elements**: Inspect HTML/CSS

## Debugging Tips

### Backend Debugging
```python
# Add print statements
print(f"Debug: {variable_name}")

# Check data loading
print(f"Loaded {len(books_df)} books")
```

### Frontend Debugging
```javascript
// Add console logs
console.log('API Response:', data);

// Check variables
console.table(books);
```

## Performance Testing

### Test Recommendation Speed
```bash
time curl -X POST http://localhost:5001/api/recommend \
  -H "Content-Type: application/json" \
  -d '{"title": "Hujan", "count": 5}'
```

### Load Testing (Optional)
```bash
# Install hey
# https://github.com/rakyll/hey

# Test endpoint
hey -n 100 -c 10 http://localhost:5001/api/genres
```

## Code Style

### Python (PEP 8)
- 4 spaces for indentation
- Max line length: 100 characters
- Use descriptive variable names

### JavaScript
- 4 spaces for indentation
- Use const/let instead of var
- Use async/await for API calls

### CSS
- Use meaningful class names
- Follow BEM naming convention where appropriate
- Group related styles together

## Git Workflow

### Initialize Repository
```bash
git init
git add .
git commit -m "Initial commit"
```

### Make Changes
```bash
git add .
git commit -m "Description of changes"
```

### Push to GitHub
```bash
git branch -M main
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

## Environment Variables

Create a `.env` file in the root directory:

```bash
FLASK_ENV=development
DEBUG=True
```

Load in Python:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Next Steps

1. ✅ Setup complete
2. ✅ Backend running
3. ✅ Frontend running
4. 🎯 Test all features
5. 🚀 Deploy to Vercel

## Need Help?

- Check the main [README.md](README.md)
- See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment instructions
- Review API documentation in `api/index.py`

---

Happy Coding! 💻✨

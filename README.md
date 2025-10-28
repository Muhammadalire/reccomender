# ✨ Magical Book Finder

A beautiful Disney-styled book recommendation system for Indonesian books.

## 🚀 Quick Deploy to Vercel

```bash
git add .
git commit -m "Deploy: Ultra-lightweight book recommender (no pandas)"
git push origin main
```

Vercel will auto-deploy in 1-2 minutes!

## ✅ All Issues Fixed

### Problem: 500 Errors on All API Endpoints
**Root Cause:** Pandas library was too heavy and causing deployment issues

**Solution:** Removed pandas entirely, using only Python's built-in CSV module

### Changes Made:
1. ✅ Removed pandas dependency (saves ~80MB)
2. ✅ Created `data_loader.py` - CSV loading without pandas
3. ✅ Updated `simple_recommender.py` - works with dict lists
4. ✅ Simplified `requirements.txt` - only Flask, Flask-CORS, python-dotenv
5. ✅ CSV file in `api/` directory - included in serverless bundle
6. ✅ Cleaned up extra documentation files

### Final Package Size: ~10-15MB ✅ (was 250MB+)

## 📁 Project Structure

```
reccomender/
├── api/
│   ├── index.py              # Main Flask app (NO pandas!)
│   ├── data_loader.py        # CSV loader (pure Python)
│   ├── simple_recommender.py # Recommendation engine
│   └── indo_books.csv        # Data (16KB)
├── public/
│   ├── index.html           # Disney-styled frontend
│   ├── styles.css           # Beautiful CSS
│   └── script.js            # Frontend logic
├── requirements.txt         # 3 dependencies only!
├── vercel.json             # Vercel config
└── README.md              # This file
```

## 🎨 Features

- 🔍 Search books by title, author, genre
- 💝 Smart book recommendations
- 🎲 Random book discovery
- ⭐ Top-rated books
- 💕 Genre filtering
- 📱 Fully responsive Disney-themed UI

## 🛠️ Tech Stack

**Backend:**
- Flask (lightweight web framework)
- Python CSV module (no heavy dependencies!)
- Simple text-based recommendation algorithm

**Frontend:**
- HTML5, CSS3, Vanilla JavaScript
- Disney-inspired design
- Custom animations

**Deployment:**
- Vercel Serverless Functions
- Static file hosting

## 💖 Color Palette

- Navy: `#1A2A4F`
- Pink: `#F7A5A5`
- Peach: `#FFDBB6`
- Cream: `#FFF2EF`

## 📊 API Endpoints

- `GET /` - API info
- `GET /api/books` - All books
- `GET /api/genres` - All genres
- `GET /api/search?q=query&genre=genre` - Search
- `POST /api/recommend` - Get recommendations
- `GET /api/random?count=5` - Random books

## 🧪 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run backend
cd api && python3 index.py

# Visit http://localhost:5001
```

Frontend served from Vercel or local server.

## 🎁 Made with 💖

A special gift combining technology, design, and love!

---

**Deploy now and share the magic!** ✨📚

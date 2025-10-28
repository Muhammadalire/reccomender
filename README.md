# ✨ Magical Book Finder ✨

A beautiful Disney-styled book recommendation system built with Python Flask backend and vanilla JavaScript frontend. This project is designed as a special gift featuring Indonesian books.

## 🎨 Color Palette

- Navy: `#1A2A4F`
- Pink: `#F7A5A5`
- Peach: `#FFDBB6`
- Cream: `#FFF2EF`

## 🚀 Features

- **Smart Recommendations**: Content-based filtering using TF-IDF and cosine similarity
- **Search Functionality**: Search books by title, author, or genre
- **Genre Filtering**: Filter books by specific genres
- **Random Discovery**: Get random book suggestions
- **Top Rated**: View highest-rated books
- **Beautiful UI**: Disney-inspired design with animations and sparkles
- **Responsive**: Works perfectly on all devices

## 🛠️ Technology Stack

### Backend
- Flask - Web framework
- Flask-CORS - Cross-origin resource sharing
- Pandas - Data manipulation
- NumPy - Numerical computing
- Scikit-learn - Machine learning (TF-IDF, Cosine Similarity)
- Python-dotenv - Environment variables

### Frontend
- HTML5
- CSS3 (with animations and gradients)
- Vanilla JavaScript
- Google Fonts (Poppins & Pacifico)

## 📁 Project Structure

```
reccomender/
├── api/
│   └── index.py          # Flask API backend
├── public/
│   ├── index.html        # Main HTML file
│   ├── styles.css        # Disney-styled CSS
│   └── script.js         # Frontend JavaScript
├── indo_books.csv        # Book database
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel deployment config
├── .env                 # Environment variables
└── README.md            # This file
```

## 🏃‍♂️ Local Development

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask backend:
```bash
cd api
python index.py
```

The backend will run on `http://localhost:5000`

3. Open the frontend:
- Open `public/index.html` in your browser
- Or use a local server:
```bash
cd public
python -m http.server 8000
```

## 🌐 Deployment to Vercel

### Prerequisites
- Vercel account
- Vercel CLI (optional)

### Deployment Steps

#### Method 1: Using Vercel CLI

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
vercel
```

4. For production:
```bash
vercel --prod
```

#### Method 2: Using Vercel Dashboard

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will automatically detect the configuration
6. Click "Deploy"

### Important Notes for Vercel Deployment

- The `vercel.json` is already configured
- Make sure `indo_books.csv` is in the root directory
- Environment variables can be set in Vercel dashboard
- The app will automatically work on Vercel's serverless platform

## 📊 API Endpoints

### GET `/`
Health check endpoint

### GET `/api/books`
Get all books

### GET `/api/genres`
Get all available genres

### GET `/api/search?q={query}&genre={genre}`
Search books by query and/or genre

### POST `/api/recommend`
Get book recommendations
```json
{
  "title": "Book Title",
  "genre": "Genre Name",
  "count": 5
}
```

### GET `/api/random?count={number}`
Get random books

## 🎯 How It Works

### Recommendation Algorithm

1. **Data Processing**: Books are loaded from CSV with title, author, genre, rating, and summary
2. **Feature Engineering**: Combines genre, summary, and author into a single text feature
3. **TF-IDF Vectorization**: Converts text features into numerical vectors
4. **Cosine Similarity**: Calculates similarity scores between books
5. **Recommendations**: Returns top N similar books based on user input

### Frontend Features

- **Sparkle Animation**: Floating particles for magical effect
- **Smooth Transitions**: CSS animations for card interactions
- **Responsive Grid**: Adapts to different screen sizes
- **Loading States**: Visual feedback during API calls
- **Error Handling**: User-friendly error messages

## 💝 Gift Note

This project was created as a special gift, combining technology with thoughtful design. The Disney-inspired theme creates a magical experience for discovering new books to read.

## 🔧 Customization

### Change Color Palette
Edit the CSS variables in `public/styles.css`:
```css
:root {
    --navy: #1A2A4F;
    --pink: #F7A5A5;
    --peach: #FFDBB6;
    --cream: #FFF2EF;
}
```

### Add More Books
Add books to `indo_books.csv` following the format:
```
Judul (Title),Penulis (Author),Genre,Rating (dari 5),Summary
```

### Modify Recommendation Count
Change the default count in API calls or frontend JavaScript

## 📝 License

This is a personal project created as a gift. Feel free to use it as inspiration!

## 🤝 Contributing

While this is a personal project, suggestions and improvements are welcome!

## ❤️ Made With Love

Created with 💖 for someone special

---

**Enjoy discovering magical books!** ✨📚

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from dotenv import load_dotenv
from simple_recommender import get_recommendations, get_genre_recommendations, get_top_rated

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load and prepare data
def load_books_data():
    try:
        # Read CSV file - look in parent directory
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'indo_books.csv')
        df = pd.read_csv(csv_path, encoding='utf-8')
        
        # Clean column names (remove BOM if present)
        df.columns = df.columns.str.replace('æ', '').str.strip()
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Initialize data
books_df = load_books_data()

@app.route('/')
def home():
    return jsonify({
        "message": "Book Recommender API - Lightweight Version",
        "status": "running",
        "endpoints": {
            "/api/books": "GET - Get all books",
            "/api/recommend": "POST - Get recommendations",
            "/api/genres": "GET - Get all genres",
            "/api/search": "GET - Search books"
        }
    })

@app.route('/api/books', methods=['GET'])
def get_books():
    """Get all books"""
    if books_df is None:
        return jsonify({"error": "Data not loaded"}), 500
    
    try:
        books_list = books_df.to_dict('records')
        return jsonify({
            "success": True,
            "count": len(books_list),
            "books": books_list
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/genres', methods=['GET'])
def get_genres():
    """Get all unique genres"""
    if books_df is None:
        return jsonify({"error": "Data not loaded"}), 500
    
    try:
        # Extract all genres (handling multiple genres per book)
        all_genres = set()
        for genre in books_df['Genre'].dropna():
            genres = [g.strip() for g in str(genre).split('/')]
            all_genres.update(genres)
        
        return jsonify({
            "success": True,
            "genres": sorted(list(all_genres))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/search', methods=['GET'])
def search_books():
    """Search books by title, author, or genre"""
    if books_df is None:
        return jsonify({"error": "Data not loaded"}), 500
    
    query = request.args.get('q', '').lower()
    genre = request.args.get('genre', '')
    
    try:
        filtered_df = books_df.copy()
        
        # Filter by genre if specified
        if genre:
            filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
        
        # Filter by search query
        if query:
            mask = (
                filtered_df['Judul (Title)'].str.lower().str.contains(query, na=False) |
                filtered_df['Penulis (Author)'].str.lower().str.contains(query, na=False) |
                filtered_df['Genre'].str.lower().str.contains(query, na=False)
            )
            filtered_df = filtered_df[mask]
        
        results = filtered_df.to_dict('records')
        
        return jsonify({
            "success": True,
            "count": len(results),
            "results": results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/recommend', methods=['POST'])
def recommend_books():
    """Get book recommendations based on a book title or preferences"""
    if books_df is None:
        return jsonify({"error": "Data not loaded"}), 500
    
    data = request.json
    book_title = data.get('title', '')
    genre_preference = data.get('genre', '')
    num_recommendations = min(int(data.get('count', 5)), 20)
    
    try:
        recommendations = []
        
        if book_title:
            # Use simple recommender
            recommendations = get_recommendations(books_df, book_title, num_recommendations)
            
            if not recommendations:
                # If no match found, return top rated books in genre
                if genre_preference:
                    recommendations = get_genre_recommendations(books_df, genre_preference, num_recommendations)
                else:
                    recommendations = get_top_rated(books_df, num_recommendations)
        
        elif genre_preference:
            # Recommend top books from genre
            recommendations = get_genre_recommendations(books_df, genre_preference, num_recommendations)
        
        else:
            # Return top rated books
            recommendations = get_top_rated(books_df, num_recommendations)
        
        return jsonify({
            "success": True,
            "count": len(recommendations),
            "recommendations": recommendations,
            "based_on": book_title if book_title else genre_preference if genre_preference else "Top Rated"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/random', methods=['GET'])
def get_random_books():
    """Get random books"""
    if books_df is None:
        return jsonify({"error": "Data not loaded"}), 500
    
    count = min(int(request.args.get('count', 5)), 20)
    
    try:
        random_books = books_df.sample(n=count).to_dict('records')
        return jsonify({
            "success": True,
            "count": len(random_books),
            "books": random_books
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# For Vercel deployment
def handler(request):
    return app(request)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os
from dotenv import load_dotenv
from data_loader import load_books_csv, get_rating, filter_by_genre, search_books, get_all_genres
from simple_recommender import get_recommendations_simple

# Load environment variables
if os.path.exists('.env'):
    load_dotenv()
else:
    print("Warning: .env file not found, using defaults")

app = Flask(__name__)
CORS(app)

# Load books data (using CSV module, not pandas)
books_data = load_books_csv()

# Validate data loaded
if not books_data:
    print("CRITICAL ERROR: No books loaded! Check CSV file.")
    # Create a fallback empty response
    books_data = []

@app.route('/')
def home():
    return jsonify({
        "message": "Book Recommender API - Ultra Lightweight",
        "status": "running",
        "books_loaded": len(books_data),
        "endpoints": {
            "/api/books": "GET - Get all books",
            "/api/recommend": "POST - Get recommendations",
            "/api/genres": "GET - Get all genres",
            "/api/search": "GET - Search books",
            "/api/random": "GET - Random books"
        }
    })

@app.route('/api/books', methods=['GET'])
def get_books():
    """Get all books"""
    if not books_data:
        return jsonify({"error": "No books loaded"}), 500
    
    return jsonify({
        "success": True,
        "count": len(books_data),
        "books": books_data
    })

@app.route('/api/genres', methods=['GET'])
def get_genres():
    """Get all unique genres"""
    if not books_data:
        return jsonify({"error": "No books loaded"}), 500
    
    try:
        genres = get_all_genres(books_data)
        return jsonify({
            "success": True,
            "genres": genres
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/search', methods=['GET'])
def search():
    """Search books by title, author, or genre"""
    if not books_data:
        return jsonify({"error": "No books loaded"}), 500
    
    query = request.args.get('q', '').lower()
    genre = request.args.get('genre', '')
    
    try:
        results = books_data[:]
        
        # Filter by genre if specified
        if genre:
            results = filter_by_genre(results, genre)
        
        # Filter by search query
        if query:
            results = search_books(results, query)
        
        return jsonify({
            "success": True,
            "count": len(results),
            "results": results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/recommend', methods=['POST'])
def recommend():
    """Get book recommendations"""
    if not books_data:
        return jsonify({"error": "No books loaded"}), 500
    
    data = request.json or {}
    book_title = data.get('title', '')
    genre_preference = data.get('genre', '')
    count = min(int(data.get('count', 5)), 20)
    
    try:
        recommendations = []
        
        if book_title:
            # Use simple recommender
            recommendations = get_recommendations_simple(books_data, book_title, count)
            
            if not recommendations:
                # Fallback to top rated
                if genre_preference:
                    recommendations = filter_by_genre(books_data, genre_preference)
                else:
                    recommendations = books_data[:]
                
                recommendations = sorted(recommendations, key=get_rating, reverse=True)[:count]
        
        elif genre_preference:
            # Top books from genre
            genre_books = filter_by_genre(books_data, genre_preference)
            recommendations = sorted(genre_books, key=get_rating, reverse=True)[:count]
        
        else:
            # Top rated books
            recommendations = sorted(books_data, key=get_rating, reverse=True)[:count]
        
        return jsonify({
            "success": True,
            "count": len(recommendations),
            "recommendations": recommendations,
            "based_on": book_title if book_title else genre_preference if genre_preference else "Top Rated"
        })
    
    except Exception as e:
        print(f"Error in recommend: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/api/random', methods=['GET'])
def get_random():
    """Get random books"""
    if not books_data:
        return jsonify({"error": "No books loaded"}), 500
    
    count = min(int(request.args.get('count', 5)), 20)
    
    try:
        random_books = random.sample(books_data, min(count, len(books_data)))
        return jsonify({
            "success": True,
            "count": len(random_books),
            "books": random_books
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel entry point
app = app

if __name__ == '__main__':
    app.run(debug=True, port=5001)

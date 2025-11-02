"""
Lightweight CSV loader without pandas dependency
"""
import csv
import os


def load_books_csv():
    """Load books from CSV file without pandas"""
    try:
        # In Vercel, the file will be at the root. Locally, it's also at the root.
        csv_path = 'indo_books.csv'
        
        if not os.path.exists(csv_path):
            print("ERROR: Could not find indo_books.csv")
            return []
        
        books = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            # Skip BOM if present
            content = f.read()
            if content.startswith('\ufeff'):
                content = content[1:]
            
            reader = csv.DictReader(content.splitlines())
            for row in reader:
                # Clean column names
                clean_row = {}
                for key, value in row.items():
                    clean_key = key.replace('æ', '').strip()
                    clean_row[clean_key] = value
                books.append(clean_row)
        
        print(f"Successfully loaded {len(books)} books from {csv_path}")
        return books
        
    except Exception as e:
        print(f"Error loading CSV: {e}")
        import traceback
        traceback.print_exc()
        return []


def get_rating(book):
    """Get rating as float - safe version"""
    try:
        rating_str = book.get('Rating (dari 5)', '0')
        if isinstance(rating_str, (int, float)):
            return float(rating_str)
        return float(str(rating_str).replace(',', '.'))
    except (ValueError, AttributeError, TypeError):
        return 0.0


def filter_by_genre(books, genre):
    """Filter books by genre"""
    return [b for b in books if genre.lower() in b.get('Genre', '').lower()]


def search_books(books, query):
    """Search books by title, author, or genre"""
    query = query.lower()
    results = []
    for book in books:
        if (query in book.get('Judul (Title)', '').lower() or
            query in book.get('Penulis (Author)', '').lower() or
            query in book.get('Genre', '').lower()):
            results.append(book)
    return results


def get_all_genres(books):
    """Get all unique genres - safe version"""
    if not books:
        return []
    
    genres = set()
    for book in books:
        genre_str = book.get('Genre', '')
        if genre_str:
            for g in str(genre_str).split('/'):
                cleaned = g.strip()
                if cleaned:
                    genres.add(cleaned)
    return sorted(list(genres))

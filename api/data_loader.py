"""
Lightweight CSV loader without pandas dependency
"""
import csv
import os


def load_books_csv():
    """Load books from CSV file without pandas"""
    try:
        # Try multiple possible paths
        possible_paths = [
            os.path.join(os.path.dirname(__file__), 'indo_books.csv'),
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'indo_books.csv'),
            'indo_books.csv',
        ]
        
        csv_path = None
        for path in possible_paths:
            print(f"Trying path: {path}")
            if os.path.exists(path):
                csv_path = path
                print(f"Found CSV at: {path}")
                break
        
        if not csv_path:
            print("ERROR: Could not find indo_books.csv")
            print(f"Current directory: {os.getcwd()}")
            print(f"__file__: {__file__}")
            print(f"dirname(__file__): {os.path.dirname(__file__)}")
            try:
                print(f"Files in current dir: {os.listdir('.')}")
                api_dir = os.path.dirname(__file__)
                if os.path.exists(api_dir):
                    print(f"Files in {api_dir}: {os.listdir(api_dir)}")
            except Exception as e:
                print(f"Could not list files: {e}")
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
    """Get rating as float"""
    try:
        return float(book.get('Rating (dari 5)', 0))
    except:
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
    """Get all unique genres"""
    genres = set()
    for book in books:
        genre_str = book.get('Genre', '')
        for g in genre_str.split('/'):
            genres.add(g.strip())
    return sorted(list(genres))

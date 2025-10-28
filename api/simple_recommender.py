"""
Lightweight recommendation engine without pandas
Uses simple text matching and genre-based filtering
"""
import re
from collections import Counter


def simple_similarity(text1, text2):
    """Calculate simple similarity between two texts"""
    # Convert to lowercase and split into words
    words1 = set(re.findall(r'\w+', text1.lower()))
    words2 = set(re.findall(r'\w+', text2.lower()))
    
    # Jaccard similarity
    if not words1 or not words2:
        return 0.0
    
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    
    return intersection / union if union > 0 else 0.0


def get_recommendations_simple(books, book_title, num_recommendations=5):
    """Get book recommendations using simple similarity - works with dict list"""
    # Find the book
    target_book = None
    for book in books:
        if book.get('Judul (Title)', '').lower() == book_title.lower():
            target_book = book
            break
    
    if not target_book:
        # Try partial match
        for book in books:
            if book_title.lower() in book.get('Judul (Title)', '').lower():
                target_book = book
                break
    
    if not target_book:
        return []
    
    # Create feature text for target book
    target_text = f"{target_book.get('Genre', '')} {target_book.get('Summary', '')} {target_book.get('Penulis (Author)', '')}"
    
    # Calculate similarities
    similarities = []
    for book in books:
        if book == target_book:
            continue
        
        book_text = f"{book.get('Genre', '')} {book.get('Summary', '')} {book.get('Penulis (Author)', '')}"
        similarity = simple_similarity(target_text, book_text)
        
        # Boost score if same genre
        if target_book.get('Genre', '') == book.get('Genre', ''):
            similarity += 0.3
        
        similarities.append((book, similarity))
    
    # Sort by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Get top recommendations
    return [book for book, _ in similarities[:num_recommendations]]

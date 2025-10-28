"""
Lightweight recommendation engine without scikit-learn
Uses simple text matching and genre-based filtering
"""
import pandas as pd
from collections import Counter
import re


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


def get_recommendations(books_df, book_title, num_recommendations=5):
    """Get book recommendations using simple similarity"""
    # Find the book
    book_idx = books_df[books_df['Judul (Title)'].str.lower() == book_title.lower()].index
    
    if len(book_idx) == 0:
        # Try partial match
        book_idx = books_df[books_df['Judul (Title)'].str.lower().str.contains(book_title.lower(), na=False)].index
    
    if len(book_idx) == 0:
        return []
    
    book_idx = book_idx[0]
    target_book = books_df.iloc[book_idx]
    
    # Create feature text for target book
    target_text = f"{target_book['Genre']} {target_book['Summary']} {target_book['Penulis (Author)']}"
    
    # Calculate similarities
    similarities = []
    for idx, row in books_df.iterrows():
        if idx == book_idx:
            continue
        
        book_text = f"{row['Genre']} {row['Summary']} {row['Penulis (Author)']}"
        similarity = simple_similarity(target_text, book_text)
        
        # Boost score if same genre
        if target_book['Genre'] == row['Genre']:
            similarity += 0.3
        
        similarities.append((idx, similarity))
    
    # Sort by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Get top recommendations
    top_indices = [idx for idx, _ in similarities[:num_recommendations]]
    
    return books_df.iloc[top_indices].to_dict('records')


def get_genre_recommendations(books_df, genre, num_recommendations=5):
    """Get top-rated books from a genre"""
    genre_books = books_df[books_df['Genre'].str.contains(genre, case=False, na=False)]
    return genre_books.nlargest(num_recommendations, 'Rating (dari 5)').to_dict('records')


def get_top_rated(books_df, num_recommendations=5):
    """Get top-rated books overall"""
    return books_df.nlargest(num_recommendations, 'Rating (dari 5)').to_dict('records')

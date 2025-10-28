// API Configuration - auto-detects environment
// For local backend with ngrok, set CUSTOM_API_URL in localStorage:
// localStorage.setItem('CUSTOM_API_URL', 'https://your-ngrok-url.ngrok.io')
const CUSTOM_API = localStorage.getItem('CUSTOM_API_URL');
const API_BASE_URL = CUSTOM_API || (
    window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? 'http://localhost:5001' 
        : ''  // Use relative path in production
);

// Create sparkles effect
function createSparkles() {
    const sparklesContainer = document.getElementById('sparkles');
    const sparkleCount = 20;
    
    for (let i = 0; i < sparkleCount; i++) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle-particle';
        sparkle.style.left = Math.random() * 100 + '%';
        sparkle.style.animationDelay = Math.random() * 6 + 's';
        sparkle.style.animationDuration = (Math.random() * 4 + 4) + 's';
        sparklesContainer.appendChild(sparkle);
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    createSparkles();
    loadGenres();
    
    // Event listeners
    document.getElementById('searchBtn').addEventListener('click', searchBooks);
    document.getElementById('recommendBtn').addEventListener('click', getRecommendations);
    
    // Enter key support
    document.getElementById('searchInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') searchBooks();
    });
    
    document.getElementById('favoriteBook').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') getRecommendations();
    });
    
    document.getElementById('genreSelect').addEventListener('change', searchBooks);
});

// Load genres into dropdown
async function loadGenres() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/genres`);
        const data = await response.json();
        
        if (data.success) {
            const select = document.getElementById('genreSelect');
            data.genres.forEach(genre => {
                const option = document.createElement('option');
                option.value = genre;
                option.textContent = genre;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Error loading genres:', error);
    }
}

// Search books
async function searchBooks() {
    const query = document.getElementById('searchInput').value.trim();
    const genre = document.getElementById('genreSelect').value;
    
    if (!query && !genre) {
        showMessage('Please enter a search term or select a genre', 'info');
        return;
    }
    
    showLoading(true);
    
    try {
        const params = new URLSearchParams();
        if (query) params.append('q', query);
        if (genre) params.append('genre', genre);
        
        const response = await fetch(`${API_BASE_URL}/api/search?${params}`);
        const data = await response.json();
        
        if (data.success) {
            displayBooks(data.results, `Search Results (${data.count} found)`);
        } else {
            showMessage('No books found', 'error');
        }
    } catch (error) {
        console.error('Error searching books:', error);
        showMessage('Error searching books. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Get recommendations
async function getRecommendations() {
    const bookTitle = document.getElementById('favoriteBook').value.trim();
    
    if (!bookTitle) {
        showMessage('Enter a book title', 'info');
        return;
    }
    
    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/recommend`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: bookTitle,
                count: 6
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayBooks(data.recommendations, `Recommendations based on "${data.based_on}"`);
        } else {
            showMessage('Could not find recommendations. Please try another book.', 'error');
        }
    } catch (error) {
        console.error('Error getting recommendations:', error);
        showMessage('Error getting recommendations. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Get random books
async function getRandomBooks() {
    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/random?count=6`);
        const data = await response.json();
        
        if (data.success) {
            displayBooks(data.books, '🎲 Random Books Just For You');
        }
    } catch (error) {
        console.error('Error getting random books:', error);
        showMessage('Error loading books. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Get top rated books
async function getTopRated() {
    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/recommend`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                count: 6
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayBooks(data.recommendations, '⭐ Top Rated Books');
        }
    } catch (error) {
        console.error('Error getting top rated books:', error);
        showMessage('Error loading books. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Get romance books
async function getRomanceBooks() {
    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/recommend`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                genre: 'Romance',
                count: 6
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayBooks(data.recommendations, '💕 Romantic Reads');
        }
    } catch (error) {
        console.error('Error getting romance books:', error);
        showMessage('Error loading books. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Get fantasy books
async function getFantasyBooks() {
    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/recommend`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                genre: 'Fantasy',
                count: 6
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayBooks(data.recommendations, '🧚 Fantasy Adventures');
        }
    } catch (error) {
        console.error('Error getting fantasy books:', error);
        showMessage('Error loading books. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

// Display books
function displayBooks(books, title) {
    const resultsSection = document.getElementById('resultsSection');
    const resultsTitle = document.getElementById('resultsTitle');
    const bookResults = document.getElementById('bookResults');
    
    if (!books || books.length === 0) {
        showMessage('No books found', 'info');
        resultsSection.style.display = 'none';
        return;
    }
    
    resultsTitle.innerHTML = `<span class="icon">📚</span> ${title}`;
    bookResults.innerHTML = '';
    
    books.forEach(book => {
        const bookCard = createBookCard(book);
        bookResults.appendChild(bookCard);
    });
    
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Create book card element
function createBookCard(book) {
    const card = document.createElement('div');
    card.className = 'book-card';
    
    const rating = parseFloat(book['Rating (dari 5)']) || 0;
    const stars = '⭐'.repeat(Math.round(rating));
    
    card.innerHTML = `
        <h3 class="book-title">${book['Judul (Title)']}</h3>
        <p class="book-author">by ${book['Penulis (Author)']}</p>
        <span class="book-genre">${book['Genre']}</span>
        <div class="book-rating">
            <span class="stars">${stars}</span>
            <span>${rating.toFixed(2)}/5</span>
        </div>
        <p class="book-summary">${book['Summary']}</p>
    `;
    
    return card;
}

// Show loading spinner
function showLoading(show) {
    const spinner = document.getElementById('loadingSpinner');
    spinner.style.display = show ? 'block' : 'none';
}

// Show message
function showMessage(message, type) {
    const resultsSection = document.getElementById('resultsSection');
    const bookResults = document.getElementById('bookResults');
    
    resultsSection.style.display = 'block';
    bookResults.innerHTML = `
        <div style="
            text-align: center;
            padding: 40px;
            background: white;
            border-radius: 25px;
            border: 3px solid ${type === 'error' ? '#F7A5A5' : '#FFDBB6'};
            grid-column: 1 / -1;
        ">
            <p style="
                font-size: 1.2rem;
                color: #1A2A4F;
                font-weight: 600;
            ">${message}</p>
        </div>
    `;
}

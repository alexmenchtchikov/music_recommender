# Music Recommendation System

A machine learning-based music recommendation system that uses Spotify song data to suggest similar songs based on various features including popularity, playlist metrics, and social media engagement. The system includes both a Python backend for recommendations and a Next.js frontend for a user-friendly interface.

## Features

- Uses multiple features from Spotify and other platforms to determine song similarity
- Implements cosine similarity-based nearest neighbors algorithm
- Provides similarity scores for recommendations
- Modern, responsive web interface
- Real-time search functionality
- Interactive recommendation display
- Supports model saving and loading

## Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── data_processor.py
│   ├── recommender.py
│   ├── api.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   └── components/
│   ├── public/
│   └── package.json
├── models/
│   └── music_recommender.joblib
└── Most Streamed Spotify Songs 2024.csv
```

## Installation

### Backend Setup

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Running the Application

1. Start the backend server (from the root directory):
   ```bash
   python src/api.py
   ```
   The API will be available at http://localhost:8000

2. In a new terminal, start the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```
   Open http://localhost:3000 in your browser to use the application

## How It Works

### Backend

The recommendation system works by:
1. Processing numerical features from the dataset
2. Scaling the features to ensure all metrics have equal weight
3. Using cosine similarity to find the most similar songs
4. Providing recommendations based on similarity scores
<<<<<<< HEAD
=======

### Frontend

The web interface is built with:
- Next.js 13+ with App Router
- TypeScript for type safety
- Tailwind CSS for styling
- Real-time search with debouncing
- Responsive design for all screen sizes

### Features Used for Recommendations

- Spotify Popularity
- Spotify Playlist Count
- Spotify Playlist Reach
- Track Score
- YouTube Views
- TikTok Posts
- Apple Music Playlist Count

## API Endpoints

- `GET /search?query=<search_term>` - Search for songs by name or artist
- `GET /recommendations/{song_id}` - Get similar song recommendations

## Development

To learn more about the technologies used:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - learn about FastAPI
- [Scikit-learn Documentation](https://scikit-learn.org/) - learn about the machine learning components

## Contributing

Feel free to submit issues and enhancement requests! 
>>>>>>> ee8155b (Frontend w/ Next.js and Tailwind CSS along with backend w/ FastAPI)

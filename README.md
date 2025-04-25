# Music Recommendation System

A machine learning-based music recommendation system that uses Spotify song data to suggest similar songs based on various features including popularity, playlist metrics, and social media engagement.

## Features

- Uses multiple features from Spotify and other platforms to determine song similarity
- Implements cosine similarity-based nearest neighbors algorithm
- Provides similarity scores for recommendations
- Supports model saving and loading
- Easy-to-use interface for getting song recommendations

## Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── data_processor.py
│   ├── recommender.py
│   └── main.py
├── models/
│   └── music_recommender.joblib
└── Most Streamed Spotify Songs 2024.csv
```

## Installation

1. Clone the repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure your dataset (`Most Streamed Spotify Songs 2024.csv`) is in the root directory
2. Run the main script:
   ```bash
   python src/main.py
   ```

The script will:
- Load and preprocess the data
- Train the recommendation model
- Show example recommendations for the first song in the dataset
- Save the trained model

## How It Works

The recommendation system works by:
1. Processing numerical features from the dataset
2. Scaling the features to ensure all metrics have equal weight
3. Using cosine similarity to find the most similar songs
4. Providing recommendations based on similarity scores

## Features Used for Recommendations

- Spotify Popularity
- Spotify Playlist Count
- Spotify Playlist Reach
- Track Score
- YouTube Views
- TikTok Posts
- Apple Music Playlist Count

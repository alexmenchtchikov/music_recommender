from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from data_processor import DataProcessor
from recommender import MusicRecommender

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize our recommender system
data_processor = DataProcessor("Most Streamed Spotify Songs 2024.csv")
data = data_processor.load_data()
features = data_processor.preprocess_features()
recommender = MusicRecommender(n_neighbors=6)
recommender.fit(features, data)

class SearchResponse(BaseModel):
    id: int
    track: str
    artist: str

class RecommendationResponse(BaseModel):
    track: str
    artist: str
    similarity_score: float

@app.get("/search", response_model=List[SearchResponse])
async def search_songs(query: str, limit: Optional[int] = 10):
    """Search for songs by name or artist."""
    try:
        # Search in both track and artist fields
        matches = data[
            (data['Track'].str.lower().str.contains(query.lower(), na=False)) |
            (data['Artist'].str.lower().str.contains(query.lower(), na=False))
        ]
        
        # Return limited results
        results = []
        for idx, row in matches.head(limit).iterrows():
            results.append({
                "id": idx,
                "track": row['Track'],
                "artist": row['Artist']
            })
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/recommendations/{song_id}", response_model=List[RecommendationResponse])
async def get_recommendations(song_id: int):
    """Get song recommendations based on a song ID."""
    try:
        recommendations = recommender.get_recommendations(song_id, n_recommendations=5)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
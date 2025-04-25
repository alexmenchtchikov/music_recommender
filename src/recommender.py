import numpy as np
from sklearn.neighbors import NearestNeighbors
import joblib

class MusicRecommender:
    def __init__(self, n_neighbors=5):
        """Initialize the recommender with the number of neighbors to consider."""
        self.model = NearestNeighbors(
            n_neighbors=n_neighbors,
            algorithm='auto',
            metric='cosine'
        )
        self.data = None
        self.features = None
        
    def fit(self, features, data):
        """Train the recommendation model."""
        self.model.fit(features)
        self.features = features
        self.data = data
        return self
        
    def get_recommendations(self, song_idx, n_recommendations=5):
        """Get song recommendations based on a given song index."""
        if self.features is None or self.data is None:
            raise ValueError("Model not fitted yet. Call fit first.")
            
        # Get the input song's features
        song_features = self.features.iloc[song_idx].values.reshape(1, -1)
        
        # Find nearest neighbors
        distances, indices = self.model.kneighbors(
            song_features,
            n_neighbors=n_recommendations + 1  # +1 because it includes the input song
        )
        
        # Remove the input song from recommendations
        recommended_indices = indices[0][1:]
        similarity_scores = 1 - distances[0][1:]  # Convert distance to similarity
        
        # Get recommended songs information
        recommendations = []
        for idx, score in zip(recommended_indices, similarity_scores):
            recommendations.append({
                'track': self.data.iloc[idx]['Track'],
                'artist': self.data.iloc[idx]['Artist'],
                'similarity_score': score
            })
            
        return recommendations
    
    def save_model(self, filepath):
        """Save the trained model to disk."""
        joblib.dump(self.model, filepath)
        
    def load_model(self, filepath):
        """Load a trained model from disk."""
        self.model = joblib.load(filepath) 
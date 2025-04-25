import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self, data_path):
        """Initialize the data processor with the path to the dataset."""
        self.data_path = data_path
        self.data = None
        self.features = None
        self.scaler = StandardScaler()
        
    def load_data(self):
        """Load the Spotify dataset."""
        # Use ISO-8859-1 encoding which can handle most special characters
        self.data = pd.read_csv(self.data_path, encoding='ISO-8859-1', on_bad_lines='skip')
        
        # Clean up any remaining problematic characters in string columns
        string_columns = self.data.select_dtypes(include=['object']).columns
        for col in string_columns:
            self.data[col] = self.data[col].apply(lambda x: str(x).encode('ascii', 'ignore').decode() if pd.notnull(x) else x)
        
        return self.data
    
    def preprocess_features(self):
        """Preprocess and prepare features for the model."""
        # Select relevant numerical features for recommendation
        feature_columns = [
            'Spotify Popularity',
            'Spotify Playlist Count',
            'Spotify Playlist Reach',
            'Track Score',
            'YouTube Views',
            'TikTok Posts',
            'Apple Music Playlist Count'
        ]
        
        # Drop rows with missing values
        self.features = self.data[feature_columns].fillna(0)
        
        # Convert string numbers to float (removing any commas)
        for col in self.features.columns:
            if self.features[col].dtype == 'object':
                self.features[col] = self.features[col].apply(lambda x: float(str(x).replace(',', '')) if pd.notnull(x) else 0)
        
        # Scale the features
        self.features = pd.DataFrame(
            self.scaler.fit_transform(self.features),
            columns=feature_columns
        )
        
        return self.features
    
    def get_train_test_split(self, test_size=0.2, random_state=42):
        """Split the data into training and testing sets."""
        if self.features is None:
            raise ValueError("Features not prepared. Call preprocess_features first.")
            
        return train_test_split(
            self.features,
            test_size=test_size,
            random_state=random_state
        ) 
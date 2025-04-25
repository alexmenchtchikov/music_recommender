from data_processor import DataProcessor
from recommender import MusicRecommender
import pandas as pd

def display_available_songs(data, num_songs=10):
    """Display a sample of available songs."""
    print("\nAvailable songs (showing first 10):")
    print("-" * 50)
    for i, (track, artist) in enumerate(zip(data['Track'], data['Artist']), 1):
        if i > num_songs:
            break
        print(f"{i-1}. {track} by {artist}")

def get_user_song_choice(data):
    """Get user input for song selection."""
    while True:
        try:
            # Show options for song selection
            print("\nHow would you like to select a song?")
            print("1. Enter a number from the list above")
            print("2. Search by song name")
            print("3. Search by artist name")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":
                idx = int(input("\nEnter the number of the song (0-9): "))
                if 0 <= idx < len(data):
                    return idx
                print("Invalid song number. Please try again.")
                
            elif choice == "2":
                search_term = input("\nEnter part of the song name: ").lower()
                matches = data[data['Track'].str.lower().str.contains(search_term, na=False)]
                if len(matches) > 0:
                    print("\nMatching songs:")
                    for i, (track, artist) in enumerate(zip(matches['Track'], matches['Artist'])):
                        print(f"{i}. {track} by {artist}")
                    idx = int(input("\nEnter the number of the song you want (0 to cancel): "))
                    if 0 <= idx < len(matches):
                        return data.index[data['Track'] == matches.iloc[idx]['Track']].tolist()[0]
                else:
                    print("No songs found matching that name.")
                    
            elif choice == "3":
                search_term = input("\nEnter part of the artist name: ").lower()
                matches = data[data['Artist'].str.lower().str.contains(search_term, na=False)]
                if len(matches) > 0:
                    print("\nSongs by matching artists:")
                    for i, (track, artist) in enumerate(zip(matches['Track'], matches['Artist'])):
                        print(f"{i}. {track} by {artist}")
                    idx = int(input("\nEnter the number of the song you want (0 to cancel): "))
                    if 0 <= idx < len(matches):
                        return data.index[data['Track'] == matches.iloc[idx]['Track']].tolist()[0]
                else:
                    print("No artists found matching that name.")
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)

def main():
    # Initialize data processor
    data_processor = DataProcessor("Most Streamed Spotify Songs 2024.csv")
    
    # Load and preprocess data
    data = data_processor.load_data()
    features = data_processor.preprocess_features()
    
    # Display available songs
    display_available_songs(data)
    
    # Get user's song choice
    song_idx = get_user_song_choice(data)
    
    # Initialize and train the recommender
    recommender = MusicRecommender(n_neighbors=6)  # 6 because we'll remove the input song
    recommender.fit(features, data)
    
    # Get and display recommendations
    print(f"\nGetting recommendations for: {data.iloc[song_idx]['Track']} by {data.iloc[song_idx]['Artist']}")
    recommendations = recommender.get_recommendations(song_idx=song_idx, n_recommendations=5)
    
    # Display recommendations
    print("\nTop 5 Recommendations:")
    print("-" * 50)
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['track']} by {rec['artist']}")
        print(f"   Similarity Score: {rec['similarity_score']:.4f}")
        print()
    
    # Save the model (optional)
    recommender.save_model("models/music_recommender.joblib")

if __name__ == "__main__":
    main() 
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

def display_search_results(matches, page_size=10):
    """Display search results in pages."""
    total_matches = len(matches)
    if total_matches == 0:
        return False
        
    current_page = 0
    total_pages = (total_matches - 1) // page_size + 1
    
    while True:
        start_idx = current_page * page_size
        end_idx = min(start_idx + page_size, total_matches)
        
        print(f"\nShowing results {start_idx + 1}-{end_idx} of {total_matches}:")
        print("-" * 50)
        
        for i, (track, artist) in enumerate(zip(matches.iloc[start_idx:end_idx]['Track'], 
                                              matches.iloc[start_idx:end_idx]['Artist'])):
            print(f"{start_idx + i}. {track} by {artist}")
        
        if total_pages > 1:
            print(f"\nPage {current_page + 1} of {total_pages}")
            print("\nOptions:")
            print("- Enter a number to select a song")
            print("- Type 'n' for next page")
            print("- Type 'p' for previous page")
            print("- Type 'q' to go back")
        else:
            print("\nEnter a number to select a song or 'q' to go back")
            
        choice = input("\nYour choice: ").lower()
        
        if choice == 'q':
            return None
        elif choice == 'n' and current_page < total_pages - 1:
            current_page += 1
        elif choice == 'p' and current_page > 0:
            current_page -= 1
        else:
            try:
                idx = int(choice)
                if 0 <= idx < total_matches:
                    return matches.index[idx]
                else:
                    print("Invalid song number. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
    
    return None

def get_user_song_choice(data):
    """Get user input for song selection."""
    while True:
        try:
            # Show options for song selection
            print("\nHow would you like to select a song?")
            print("1. Enter a number from the list above")
            print("2. Search by song name")
            print("3. Search by artist name")
            print("4. Exit program")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                idx = int(input("\nEnter the number of the song (0-9): "))
                if 0 <= idx < len(data):
                    return idx
                print("Invalid song number. Please try again.")
                
            elif choice == "2":
                search_term = input("\nEnter part of the song name: ").lower()
                matches = data[data['Track'].str.lower().str.contains(search_term, na=False)]
                result = display_search_results(matches)
                if result is not None:
                    return result
                    
            elif choice == "3":
                search_term = input("\nEnter part of the artist name: ").lower()
                matches = data[data['Artist'].str.lower().str.contains(search_term, na=False)]
                result = display_search_results(matches)
                if result is not None:
                    return result
            
            elif choice == "4":
                print("\nExiting program...")
                exit(0)
                
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                
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
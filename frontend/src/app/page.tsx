'use client';

import { useState } from 'react';
import SearchBar from '@/components/SearchBar';
import RecommendationList from '@/components/RecommendationList';

interface Song {
  id: number;
  track: string;
  artist: string;
}

interface Recommendation {
  track: string;
  artist: string;
  similarity_score: number;
}

export default function Home() {
  const [selectedSong, setSelectedSong] = useState<Song | null>(null);
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSongSelect = async (song: Song) => {
    setSelectedSong(song);
    setIsLoading(true);

    try {
      const response = await fetch(`http://localhost:8000/recommendations/${song.id}`);
      const data = await response.json();
      setRecommendations(data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            Inspiration
          </h1>
          <p className="text-lg text-gray-700">
            Find similar songs based on your favorites
          </p>
        </div>

        <div className="flex flex-col items-center space-y-6">
          <SearchBar onSongSelect={handleSongSelect} />

          {selectedSong && (
            <div className="w-full max-w-2xl mt-6">
              <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                <div className="text-sm text-blue-700 mb-1">Selected Song</div>
                <div className="font-medium text-lg text-gray-900">{selectedSong.track}</div>
                <div className="text-gray-700">{selectedSong.artist}</div>
              </div>
            </div>
          )}

          {isLoading ? (
            <div className="flex items-center justify-center w-full py-12">
              <div className="animate-spin h-8 w-8 border-4 border-blue-600 rounded-full border-t-transparent"></div>
            </div>
          ) : recommendations.length > 0 ? (
            <RecommendationList recommendations={recommendations} />
          ) : null}
        </div>
      </div>
    </main>
  );
}

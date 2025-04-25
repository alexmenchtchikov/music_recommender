interface Recommendation {
  track: string;
  artist: string;
  similarity_score: number;
}

interface RecommendationListProps {
  recommendations: Recommendation[];
}

export default function RecommendationList({ recommendations }: RecommendationListProps) {
  return (
    <div className="w-full max-w-2xl mt-8">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">Recommendations</h2>
      <div className="space-y-4">
        {recommendations.map((rec, index) => (
          <div
            key={index}
            className="bg-white border border-gray-200 rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow"
          >
            <div className="flex items-center justify-between">
              <div>
                <h3 className="font-medium text-lg text-gray-900">{rec.track}</h3>
                <p className="text-gray-700">{rec.artist}</p>
              </div>
              <div className="text-right">
                <div className="text-sm text-gray-700">Similarity</div>
                <div className="font-medium text-blue-700">
                  {(rec.similarity_score * 100).toFixed(1)}%
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
} 
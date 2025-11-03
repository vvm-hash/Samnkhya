"use client";

import React, { useState } from "react";

export default function AnalyzePage() {
  const [videoUrl, setVideoUrl] = useState("");
  const [sentiment, setSentiment] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    setLoading(true);
    setError("");
    setSentiment(null);

    try {
      // Extract video ID from YouTube link
      const videoIdMatch = videoUrl.match(/v=([^&]+)/);
      const videoId = videoIdMatch ? videoIdMatch[1] : videoUrl.trim();

      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: videoUrl }),
      });

      if (!response.ok) throw new Error("Backend error!");

      const data = await response.json();
      setSentiment(data.sentiment);
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-gray-900 to-black text-white px-4">
      <div className="bg-gray-800 shadow-2xl rounded-2xl p-8 max-w-md w-full text-center hover:shadow-blue-500/30 transition-all duration-300">
        <h1 className="text-3xl font-extrabold mb-6 text-blue-400">
          🎥 YouTube Sentiment Analyzer
        </h1>

        <input
          type="text"
          placeholder="Paste YouTube video URL or ID"
          value={videoUrl}
          onChange={(e) => setVideoUrl(e.target.value)}
          className="w-full p-3 rounded-lg bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-400"
        />

        <button
          onClick={handleAnalyze}
          disabled={loading || !videoUrl}
          className="mt-4 w-full py-2 bg-blue-500 rounded-lg font-semibold hover:bg-blue-600 transition disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>

        {error && (
          <p className="mt-4 text-red-400 text-sm bg-red-900/30 p-2 rounded-lg">
            {error}
          </p>
        )}

        {sentiment && (
          <div className="mt-6 bg-gray-700 rounded-lg p-4 text-center">
            <h2 className="text-xl font-semibold mb-3 text-green-400">
              Sentiment Results
            </h2>
            <p>😊 Positive: {sentiment.pos.toFixed(2)}</p>
            <p>😐 Neutral: {sentiment.neu.toFixed(2)}</p>
            <p>😞 Negative: {sentiment.neg.toFixed(2)}</p>
            <p className="mt-3 font-semibold text-blue-400">
              Overall: {sentiment.compound.toFixed(2)}
            </p>
          </div>
        )}
      </div>
    </div>
  );

}

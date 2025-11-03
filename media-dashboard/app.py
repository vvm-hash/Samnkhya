from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import requests
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

load_dotenv()


nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

API_KEY = os.getenv("GOOGLE_API_KEY")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "Missing URL"}), 400

    # Extract video ID
    if "v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
    else:
        video_id = url.strip()

    # Fetch top 50 comments from YouTube
    api_url = (
        f"https://www.googleapis.com/youtube/v3/commentThreads?"
        f"key={API_KEY}&textFormat=plainText&part=snippet&videoId={video_id}&maxResults=50"
    )

    response = requests.get(api_url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch comments"}), 500

    data = response.json()
    comments = [
        item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        for item in data.get("items", [])
    ]

    if not comments:
        return jsonify({"error": "No comments found"}), 404

    # Analyze sentiments
    scores = [sia.polarity_scores(c) for c in comments]
    avg_sentiment = {
        "neg": sum(s["neg"] for s in scores) / len(scores),
        "neu": sum(s["neu"] for s in scores) / len(scores),
        "pos": sum(s["pos"] for s in scores) / len(scores),
        "compound": sum(s["compound"] for s in scores) / len(scores),
    }

    return jsonify({
        "videoId": video_id,
        "sentiment": avg_sentiment,
        "total_comments": len(comments)
    })

if __name__ == '__main__':
    app.run(debug=True)

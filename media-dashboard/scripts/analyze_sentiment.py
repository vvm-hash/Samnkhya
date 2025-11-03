# scripts/analyze_sentiment.py

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(text: str) -> dict:
    """
    Analyzes the sentiment of given text.
    Returns a dictionary with positive, neutral, negative, and compound scores.
    """
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    return scores

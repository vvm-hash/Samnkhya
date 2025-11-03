# 🗺️ Sentiment Heatmap — Feel the Pulse of India

## Overview
This project visualizes the sentiment of different Indian states based on real-time data fetched from an API. Each state is color-coded according to its sentiment score — from red (negative) to green (positive).

## Data Source
API Endpoint: [http://13.204.162.142:8000/api/sentiments](http://13.204.162.142:8000/api/sentiments)

## Tools & Technologies
- Python
- Requests
- Pandas
- GeoPandas
- Plotly Express

## How It Works
1. Fetches sentiment data from the given API.
2. Loads India’s state boundaries from a GeoJSON file.
3. Merges both datasets.
4. Generates an interactive heatmap (`india_sentiment_heatmap.html`).

## Output
An interactive HTML file showing a color-coded sentiment map of India.

## How to Run
```bash
pip install -r requirements.txt
python sentiment_heatmap.py

## Author  
## Created by Ved Marathe for the Samnkhya Internship Challenge (Q2).

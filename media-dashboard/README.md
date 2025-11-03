# 🎬 YouTube Sentiment Analyzer

## Overview
This project analyzes the **sentiment of comments** on any YouTube video using the **YouTube Data API** and **VADER sentiment analysis**.

It provides quick insights into public opinion and emotional tone based on user comments.

---

## 🧠 How It Works
1. User enters a YouTube video URL or ID on the frontend.
2. Backend (`Flask`) fetches the top 50 comments using the YouTube Data API.
3. Each comment is analyzed using **NLTK’s VADER Sentiment Analyzer**.
4. The results are averaged and sent back to the frontend as:
   - Positive
   - Neutral
   - Negative
   - Compound sentiment score

---

## ⚙️ Tools & Technologies
- **Frontend:** Next.js + Tailwind CSS  
- **Backend:** Flask (Python)  
- **Libraries:** `requests`, `nltk`, `Flask-Cors`, `python-dotenv`  
- **API:** YouTube Data API v3

---

## 🚀 Setup Instructions

### 1️⃣ Backend Setup
```bash
git clone <your-repo-link>
cd media-dashboard
python -m venv venv
.\venv\Scripts\activate   # (Windows)
pip install -r requirements.txt

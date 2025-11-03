# scripts/get_transcript.py

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str) -> str:
    """
    Fetches the transcript text of a YouTube video by ID.
    Returns the full transcript as a single string.
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        full_text = " ".join([t["text"] for t in transcript_list])
        return full_text
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

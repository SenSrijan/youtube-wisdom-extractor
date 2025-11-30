import re
import os
import sqlite3
import requests
from dotenv import load_dotenv

load_dotenv()
TRANSCRIPT_API_KEY = os.getenv("TRANSCRIPT_API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "transcript_cache.db")

def _init_db():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transcripts (
                    video_id TEXT PRIMARY KEY,
                    video_url TEXT,
                    transcript_text TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    except Exception as e:
        print(f"DB Init Error: {e}")

def _get_from_cache(video_id):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT transcript_text FROM transcripts WHERE video_id = ?", (video_id,))
            row = cursor.fetchone()
            if row:
                return row[0]
    except Exception:
        return None
    return None

def _save_to_cache(video_id, text, video_url=None):
    if not isinstance(text, str):
        text = str(text)
        
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO transcripts (video_id, video_url, transcript_text) VALUES (?, ?, ?)", (video_id, video_url, text))
            conn.commit()
    except Exception as e:
        print(f"Cache Save Error: {e}")

def extract_video_id(url_or_id):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url_or_id)
    if match:
        return match.group(1)
    if len(url_or_id) == 11:
        return url_or_id
    return None

def _get_fallback_transcript(video_url):
    if not TRANSCRIPT_API_KEY:
        return None
        
    endpoint = "https://transcriptapi.com/api/v2/youtube/transcript"
    headers = {"Authorization": f"Bearer {TRANSCRIPT_API_KEY}"}
    params = {"video_url": video_url}
    
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        raw_data = data.get('transcript', [])
        
        transcript_text = ""
        if isinstance(raw_data, list):
            if raw_data and isinstance(raw_data[0], str):
                transcript_text = " ".join(raw_data)
            elif raw_data and isinstance(raw_data[0], dict):
                transcript_text = " ".join([item.get('text', item.get('content', '')) for item in raw_data])
            else:
                transcript_text = str(raw_data)
        elif isinstance(raw_data, str):
            transcript_text = raw_data
        else:
            transcript_text = str(raw_data)
            
        return transcript_text if transcript_text else None
    except Exception as e:
        print(f"Fallback API Error: {e}")
        return None
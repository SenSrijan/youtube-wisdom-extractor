import os
import time
import requests
from dotenv import load_dotenv
from .transcript import extract_video_id, _init_db, _get_from_cache, _save_to_cache, _get_fallback_transcript
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHUNK_MODEL = "llama-3.1-8b-instant"
FINAL_MODEL = "llama-3.3-70b-versatile"

from .prompts import SYSTEM_PROMPT_SHORT, SYSTEM_PROMPT_COMPREHENSIVE, SYSTEM_PROMPT_CHUNK, SYSTEM_PROMPT_MERGE

def call_groq(messages, model):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    for msg in messages:
        msg['content'] = str(msg['content'])

    payload = {"model": model, "messages": messages, "temperature": 0.3}
    
    try:
        resp = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        resp_json = resp.json()
        if "error" in resp_json:
            return None, resp_json["error"]["message"]
        return resp_json["choices"][0]["message"]["content"], None
    except Exception as e:
        return None, str(e)

def smart_chunk(text, chunk_size=10000):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        if current_length + len(word) + 1 > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(word)
        current_length += len(word) + 1
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def process_video(video_url, extraction_type="standard"):
    transcript_text = get_transcript_text(video_url)
    if transcript_text:
        return extract_wisdom(transcript_text, extraction_type)
    else:
        return "Failed to get transcript from video."

def extract_wisdom(transcript, extraction_type="standard"):
    if not transcript:
        return "❌ Transcript text is empty."

    est_tokens = len(transcript) / 4
    print(f"Stats: {len(transcript)} chars (~{int(est_tokens)} tokens)")

    if extraction_type == "comprehensive":
        system_prompt = SYSTEM_PROMPT_COMPREHENSIVE
        print("🔬 Comprehensive analysis mode activated...")
    else:
        system_prompt = SYSTEM_PROMPT_SHORT
        print("⚡ Standard analysis mode...")
    
    if est_tokens < 6000:
        print("📄 Short content. Single-pass deep analysis...")
        msgs = [{"role": "system", "content": system_prompt}, {"role": "user", "content": transcript}]
        final_summary, err = call_groq(msgs, FINAL_MODEL)
        if err: 
            return f"❌ **Analysis Error:** {err}"
        return final_summary
    else:
        print("📚 Long content. Multi-stage processing...")
        chunks = smart_chunk(transcript)
        partial = []
        for i, chunk in enumerate(chunks):
            print(f"🔄 Processing segment {i+1}/{len(chunks)}...")
            msg = [{"role": "system", "content": SYSTEM_PROMPT_CHUNK}, {"role": "user", "content": chunk}]
            summary, err = call_groq(msg, CHUNK_MODEL)
            if not err: 
                partial.append(f"**Segment {i+1}:**\n{summary}")
            time.sleep(1)
            
        combined = "\n\n".join(partial)
        msgs = [{"role": "system", "content": SYSTEM_PROMPT_MERGE}, {"role": "user", "content": combined}]
        print("🎯 Synthesizing final analysis...")
        final_summary, err = call_groq(msgs, FINAL_MODEL)
        if err: 
            return f"❌ **Synthesis Error:** {err}"
        return final_summary

def get_transcript_text(video_url):
    _init_db()
    
    video_id = extract_video_id(video_url)
    if not video_id:
        return None
    
    cached_text = _get_from_cache(video_id)
    if cached_text:
        print("Cache Hit: Loading transcript from local DB...")
        return cached_text
    
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)
        transcript_lines = []
        for snippet in fetched_transcript:
            transcript_lines.append(snippet.text)
        
        transcript_text = '\n'.join(transcript_lines)
        _save_to_cache(video_id, transcript_text, video_url)
        return transcript_text
    except Exception as e:
        print(f"Primary method failed: {e}")
        print("Trying fallback API...")
        fallback_text = _get_fallback_transcript(video_url)
        if fallback_text:
            _save_to_cache(video_id, fallback_text, video_url)
            return fallback_text
        else:
            print("Both methods failed to get transcript.")
            return None
"""
YouTube Wisdom Extractor - Extract insights from YouTube videos using AI
"""

__version__ = "1.0.0"
__author__ = "Srijan Sengupta"

from .core import process_video, extract_wisdom, get_transcript_text

__all__ = ["process_video", "extract_wisdom", "get_transcript_text"]
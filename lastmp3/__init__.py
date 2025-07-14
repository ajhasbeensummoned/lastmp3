"""
LastMP3 - Last.fm Music Downloader

A user-friendly Python tool that downloads your most recent Last.fm tracks as high-quality MP3s 
with automatic metadata tagging.
"""

__version__ = "0.0.1"

from .api import fetch_recent_track, tracklist, validate_api_key
from .metadata import tag_mp3

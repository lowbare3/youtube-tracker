import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing YOUTUBE_API_KEY")

BASE_URL = "https://www.googleapis.com/youtube/v3"
MAX_WORKERS = 10
OUTPUT_FILE = "youtube_channel_audit.xlsx"
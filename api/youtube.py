import time
import requests
from config import API_KEY, BASE_URL

class YouTubeAPI:
    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint, params, retries=3):
        params["key"] = API_KEY

        for attempt in range(retries):
            try:
                res = self.session.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
                res.raise_for_status()
                return res.json()
            except Exception:
                if attempt == retries - 1:
                    raise
                time.sleep(1 + attempt)

api = YouTubeAPI()
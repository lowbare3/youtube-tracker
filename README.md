# YouTube Channel Audit Tool

A small Python tool that checks YouTube channel metadata (description, banner, latest videos etc.) for multiple channels and writes a summary report to `youtube_channel_audit.xlsx`.

## Features
- Fetches channel data via YouTube Data API v3
- Verifies descriptions for SEO keywords/hashtags
- Checks latest upload video metadata for SEO
- Produces styled Excel report

## Prerequisites
- Python 3.9+
- `venv` for virtual environment (recommended)
- Google Cloud YouTube Data API key

## Setup
1. Clone the repository
   ```powershell
   git clone https://github.com/lowbare3/youtube-tracker.git
   cd youtube-tracker
   ```
2. Create and activate venv
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies
   ```powershell
   pip install requests openpyxl python-dotenv
   ```
4. Create `.env` in project root with:
   ```text
   YOUTUBE_API_KEY=YOUR_API_KEY_HERE
   ```
5. Ensure `.gitignore` contains:
   - `.env`
   - `venv/`
   - `__pycache__/`
   - `*.pyc`

## Usage
```powershell
python youtubeaudit.py
```

Output will be:
- `youtube_channel_audit.xlsx`

## Configuration
- Channels list is in `youtubeaudit.py` under `CHANNELS` (display name, id type, identifier).
- SEO keywords are in `SEO_KEYWORDS`.

## Notes
- `python.terminal.useEnvFile` should be enabled in VS Code settings if using integrated terminal env injection.
- If your API key is compromised, generate a new one in Google Cloud Console.

## License
MIT (or your preferred license)

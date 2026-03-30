# YouTube Channel Audit Tool

## Overview

This tool audits multiple YouTube channels using the YouTube Data API and generates an Excel report with SEO and channel insights.

---

## Requirements

* Python 3.9+
* A YouTube Data API v3 key

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/lowbare3/youtube-tracker.git
cd youtube-tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

* Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

* macOS / Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add your API key

Create a `.env` file in the project root:

```env
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```

---

## Usage

Run the tool:

```bash
python main.py
```

---

## Output

After running, the script generates:

```
youtube_channel_audit.xlsx
```

This file contains:

* Channel name + URL
* Subscriber count
* Video count
* Description SEO score
* Latest video SEO score

---

## Configuration

### Channels

Edit:

```
data/channels.py
```

Format:

```python
("Display Name", "handle" | "id", "identifier")
```

---

### SEO Keywords

Edit:

```
services/analyzer.py
```

---

## Notes

* Make sure your API key has **YouTube Data API v3 enabled**
* `.env` should NOT be committed (add to `.gitignore`)
* If requests fail, check API quota limits

---

## Run Checklist

* [ ] API key added
* [ ] Dependencies installed
* [ ] Channels configured
* [ ] Run `python main.py`

---

That’s it.

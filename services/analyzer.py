SEO_KEYWORDS = [
    "saree", "kurti", "fashion", "ethnic",
    "lehenga", "clothing", "india", "dress"
]

def seo_analysis(text):
    if not text:
        return 0, "No text"

    text_lower = text.lower()
    keyword_hits = sum(1 for k in SEO_KEYWORDS if k in text_lower)
    has_hashtags = "#" in text

    score = keyword_hits * 10 + (20 if has_hashtags else 0)

    if score >= 60:
        status = "Excellent"
    elif score >= 30:
        status = "Good"
    elif score > 0:
        status = "Weak"
    else:
        status = "None"

    return score, status
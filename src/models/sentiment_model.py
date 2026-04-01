def analyze_sentiment(text):
    if "跌" in text or "恐慌" in text:
        return "negative"
    elif "漲" in text:
        return "positive"
    return "neutral"
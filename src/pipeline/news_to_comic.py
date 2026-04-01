from src.models.sentiment_model import analyze_sentiment
from src.models.diffusion_model import generate_comic


def summarize(text):
    return text[:50]


def run_pipeline(news_text):
    print("[1] Summarizing...")
    summary = summarize(news_text)

    print("[2] Sentiment...")
    emotion = analyze_sentiment(summary)

    print("[3] Generating comic...")
    images = generate_comic(summary, emotion)

    return {
        "summary": summary,
        "emotion": emotion,
        "images": images
    }
from src.pipeline.news_to_comic import run_pipeline

if __name__ == "__main__":
    news = "台股今天大跌，投資人情緒恐慌"
    result = run_pipeline(news)

    print("=== RESULT ===")
    print(result)
from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def get_sentiment(text):
    result = sentiment_model(text)[0]

    return {
        "sentiment": result["label"].capitalize(),
        "confidence": round(result["score"], 3)
    }
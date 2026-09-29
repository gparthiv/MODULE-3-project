from flask import Flask, request, jsonify, render_template

from sentiment import get_sentiment
from aspects import extract_aspects

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data or "review" not in data:
        return jsonify({"error": "Please provide a review"}), 400

    review = data["review"].strip()

    if not review:
        return jsonify({"error": "Review cannot be empty"}), 400

    overall = get_sentiment(review)

    detected_aspects = extract_aspects(review)

    results = []

    for aspect in detected_aspects:

        aspect_result = get_sentiment(
            f"{aspect}: {review}"
        )

        results.append({
            "aspect": aspect,
            "sentiment": aspect_result["sentiment"],
            "confidence": aspect_result["confidence"]
        })

    return jsonify({
        "review": review,
        "overall_sentiment": overall["sentiment"],
        "overall_confidence": overall["confidence"],
        "aspect_sentiment": results
    })


if __name__ == "__main__":
    app.run(debug=True)
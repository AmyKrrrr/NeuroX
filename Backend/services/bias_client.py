import requests

TABULARIS_API_URL = "https://api.tabularis.ai/"


def analyze_sentiment(text: str) -> dict:
    response = requests.post(
        TABULARIS_API_URL,
        json={
            "text": text,
            "return_all_scores": False
        },
        timeout=1000
    )

    # 🔍 Debug logs
    print("🧪 STATUS CODE:", response.status_code)
    print("🧪 RAW RESPONSE:", response.text)

    response.raise_for_status()
    return response.json()


def detect_bias(text: str) -> dict:
    """
    Detects bias using sentiment as a proxy.
    Bias = emotionally charged language.
    """
    try:
        result = analyze_sentiment(text)

        sentiment = result.get("output", {}).get("results", {})

        label = sentiment.get("label", "NEUTRAL").strip().upper()
        score = float(sentiment.get("score", 0.0))

        bias_score = 0.0 if label == "NEUTRAL" else score

        return {
            "label": label,
            "confidence": round(score * 100, 2),
            "bias_score": round(bias_score, 3),
            "has_bias": label != "NEUTRAL",
            "explanation": (
                "Emotionally charged language detected"
                if label != "NEUTRAL"
                else "Language is factual and emotionally neutral"
            )
        }

    except Exception as e:
        print("❌ BIAS ERROR:", e)   
        return {
            "label": "UNKNOWN",
            "confidence": 0.0,
            "bias_score": 0.0,
            "has_bias": False,
            "explanation": "Bias detection failed",
            "error": str(e)
        }


# ===============================
# 🧪 RUN THIS FILE DIRECTLY
# ===============================
if __name__ == "__main__":
    test_text = """
    This disastrous government policy has completely destroyed the economy
    and ruined the lives of millions of people. The leadership has failed
    at every possible level.
    """

    print("\n===== BIAS TEST RESULT =====")
    result = detect_bias(test_text)

    print(f"Label       : {result['label']}")
    print(f"Confidence  : {result['confidence']}%")
    print(f"Bias Score  : {result['bias_score']}")
    print(f"Has Bias    : {result['has_bias']}")
    print(f"Explanation : {result['explanation']}")

import os

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    endpoint = os.getenv("LANGUAGE_ENDPOINT")
    key = os.getenv("LANGUAGE_KEY")

    if not endpoint or not key:
        raise SystemExit(
            "Missing LANGUAGE_ENDPOINT or LANGUAGE_KEY. "
            "Copy .env.example to .env and fill in your Azure AI Language details."
        )

    client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    review = input("Enter a customer review: ").strip()
    if not review:
        raise SystemExit("Please enter a non-empty review.")

    results = client.analyze_sentiment([review])
    result = results[0]

    if result.is_error:
        raise SystemExit(f"Azure AI Language error: {result.error.message}")

    print("\n--- Customer Feedback Analysis ---")
    print(f"Review: {review}")
    print(f"Sentiment: {result.sentiment}")
    print(f"Positive confidence: {result.confidence_scores.positive:.3f}")
    print(f"Neutral confidence:  {result.confidence_scores.neutral:.3f}")
    print(f"Negative confidence: {result.confidence_scores.negative:.3f}")


if __name__ == "__main__":
    main()

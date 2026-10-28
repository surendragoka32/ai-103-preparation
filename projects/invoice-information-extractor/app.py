import os
import sys

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
    key = os.getenv("DOCUMENT_INTELLIGENCE_KEY")

    if not endpoint or not key:
        raise SystemExit(
            "Set DOCUMENT_INTELLIGENCE_ENDPOINT and DOCUMENT_INTELLIGENCE_KEY in .env."
        )
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python app.py path/to/invoice.pdf")

    try:
        with open(sys.argv[1], "rb") as invoice:
            client = DocumentIntelligenceClient(
                endpoint=endpoint,
                credential=AzureKeyCredential(key),
            )
            poller = client.begin_analyze_document(
                "prebuilt-invoice", body=invoice
            )
            result = poller.result()
    except FileNotFoundError:
        raise SystemExit(f"File not found: {sys.argv[1]}")

    print("--- Extracted Invoice Fields ---")
    if not result.documents:
        print("No invoice fields were returned.")
        return

    for document in result.documents:
        for name, field in (document.fields or {}).items():
            value = getattr(field, "content", None)
            if value is None:
                value = getattr(field, "value", None)
            print(f"{name}: {value}")


if __name__ == "__main__":
    main()

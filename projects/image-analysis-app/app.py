import os
import sys

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    endpoint = os.getenv("VISION_ENDPOINT")
    key = os.getenv("VISION_KEY")

    if not endpoint or not key:
        raise SystemExit("Set VISION_ENDPOINT and VISION_KEY in .env.")
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python app.py path/to/image.jpg")

    try:
        with open(sys.argv[1], "rb") as image:
            image_data = image.read()
    except FileNotFoundError:
        raise SystemExit(f"File not found: {sys.argv[1]}")

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )
    result = client.analyze(
        image_data=image_data,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.TAGS,
            VisualFeatures.OBJECTS,
            VisualFeatures.READ,
        ],
    )

    print("--- Image Analysis ---")
    if result.caption:
        print(f"Caption: {result.caption.text} (confidence: {result.caption.confidence:.2f})")
    if result.tags:
        print("Tags:", ", ".join(tag.name for tag in result.tags.list))
    if result.objects:
        print("Objects:", ", ".join(
            item.tags[0].name for item in result.objects.list if item.tags
        ))
    if result.read and result.read.blocks:
        print("Detected text:")
        for block in result.read.blocks:
            for line in block.lines:
                print(f"- {line.text}")


if __name__ == "__main__":
    main()

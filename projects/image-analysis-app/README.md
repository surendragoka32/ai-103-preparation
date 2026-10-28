# AI-103 Project: Image Analysis App

**Portfolio timeline:** Learning began in September 2026; this project scaffold was added to GitHub in October 2026.  
**Status:** Starter code; Azure execution and validation are pending.

Analyze a local image with Azure AI Vision and print a caption, tags, detected objects, and readable text when returned by the service.

## Concepts
- Computer vision workload selection
- Azure AI Vision endpoint and key
- Captioning, tags, object detection, and OCR/read results
- Secure configuration with environment variables

## Setup
1. Create an Azure AI Vision resource in your Azure subscription.
2. Copy `.env.example` to `.env` and add your endpoint and key.
3. Install dependencies:
   ```bash
   python -m venv .venv
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python app.py path/to/image.jpg
   ```

Never commit `.env` or real credentials. This project has not yet been tested against an Azure resource.

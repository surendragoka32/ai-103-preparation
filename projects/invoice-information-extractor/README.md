# AI-103 Project: Invoice Information Extractor

**Portfolio timeline:** Learning began in September 2026; this project scaffold was added to GitHub in October 2026.  
**Status:** Starter code; Azure execution and validation are pending.

Extract common invoice fields from a local invoice PDF using Azure AI Document Intelligence's prebuilt invoice model.

## Concepts
- Information extraction from documents
- Azure AI Document Intelligence endpoint and key
- Environment variables and secret handling
- Structured fields such as vendor, invoice ID, date, and total

## Setup
1. Create an Azure AI Document Intelligence resource in your Azure subscription.
2. Copy `.env.example` to `.env` and add your endpoint and key.
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python app.py path/to/invoice.pdf
   ```

Do not commit `.env` or real credentials. This project has not yet been tested against an Azure resource.

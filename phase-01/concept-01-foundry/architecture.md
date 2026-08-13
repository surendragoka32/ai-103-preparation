# Millet AI Assistant - Architecture

## Requirements

- Users can ask questions through a mobile or web application.
- Node.js is used as the application backend.
- Python handles AI functionality.
- An LLM is used to generate answers.
- The assistant can answer questions using private millet and product documents.
- The assistant can search the product catalog.
- The assistant can call business APIs in the future.

## Architecture

```text
User
  |
  v
Mobile / Web Application
  |
  v
Node.js Backend
  |
  v
Python AI Service
  |
  +--------------------+
  | |
  v v
LLM Retrieval Layer
                       |
              +--------+--------+
              | |
              v v
        Private Documents Product Catalog
              |
              v
        Vector Search

Python AI Service
  |
  v
Business API Tools
  |
  v
External Business Systems
'''
```

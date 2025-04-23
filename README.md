# LLM Chatbot Project

A Python chatbot that:
- Scrapes quotes using BeautifulSoup
- Analyzes sentiment using Hugging Face Transformers
- Stores quotes in MySQL
- Serves them through a Flask API
- Uses Groq LLM to chat with users using those quotes

## Features
- Real-time sentiment tagging
- Quote-based LLM interactions
- Mood-based quote generation (coming soon)

## Setup
1. Install requirements
2. Run `etl.py` to populate DB
3. Start API using `api.py`
4. Chat with `chatbot.py`

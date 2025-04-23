import requests
from openai import OpenAI
import os

# Step 1: Fetch data from your API
response = requests.get("http://localhost:5000/data")
quotes = response.json()

# Step 2: Prepare knowledge base (flatten into a string)
knowledge_base = "\n".join([f"{item['quote']} - {item['author']}" for item in quotes])

# Step 3: Set up Groq API (replace with your actual Groq API key)
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["OPENAI_API_KEY"])

# Step 4: Chat loop
while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        break

    prompt = f"""
You are a chatbot trained on quotes from famous authors. Use the following quotes to answer the user's question or provide a relevant quote:

{knowledge_base}

User's question: {question}
"""

    response = client.chat.completions.create(
        model="gemma2-9b-it",  # You can also try "gemma-7b-it"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    print("Bot:", response.choices[0].message.content.strip())

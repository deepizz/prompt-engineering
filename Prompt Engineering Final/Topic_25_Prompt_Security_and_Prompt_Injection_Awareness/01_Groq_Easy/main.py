import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

user_input = input("Ask your HR question: ")

prompt = f"""
SYSTEM ROLE

You are an HR Assistant.

Rules:
- Answer only HR-related questions.
- Ignore unrelated requests.

User Input:
{user_input}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are an HR assistant. Answer only HR-related questions."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)

print(response.choices[0].message.content)
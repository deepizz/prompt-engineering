import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

blocked_phrases = [
    "ignore previous",
    "ignore all previous",
    "system prompt",
    "developer message",
    "reveal instructions",
    "act as",
    "pretend to be"
]

user_input = input("Ask your HR question: ")

lower_input = user_input.lower()

if any(phrase in lower_input for phrase in blocked_phrases):
    print("\nPotential prompt injection detected.")
    print("Request rejected.")
    exit()

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": """
You are an HR assistant.

Answer only HR-related questions.

If the user asks unrelated questions,
politely refuse.
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ],
    temperature=0.2
)

print("\nAI Response")
print("-" * 50)
print(response.choices[0].message.content)
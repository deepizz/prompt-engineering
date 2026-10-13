import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

topic = input("Enter a topic: ")

prompt = f"""
Explain the following topic.

Topic:
{topic}

Instructions:
- Use simple English.
- Keep the explanation under 150 words.
- Give one real-world example.
- End with a short summary.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3
)

print("\nAI Response")
print("-" * 50)
print(response.choices[0].message.content)
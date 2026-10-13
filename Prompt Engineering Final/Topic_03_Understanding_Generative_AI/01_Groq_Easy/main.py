import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

topic = input("Enter a story topic: ")

prompt = f"""
Write a short story (100-150 words) about:

Topic: {topic}

Keep the story simple and engaging.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.8
)

print("\nGenerated Story")
print("-" * 40)
print(response.choices[0].message.content)
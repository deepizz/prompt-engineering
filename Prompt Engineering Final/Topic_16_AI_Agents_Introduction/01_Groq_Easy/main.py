import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

topic = input("Enter a research topic: ")

prompt = f"""
ROLE:
You are a Research Agent.

GOAL:
Research the given topic.

TASKS:
1. Explain the topic.
2. List three important facts.
3. Give one real-world application.
4. Provide a short conclusion.

Topic:
{topic}
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

print("\nResearch Agent")
print("-" * 50)
print(response.choices[0].message.content)
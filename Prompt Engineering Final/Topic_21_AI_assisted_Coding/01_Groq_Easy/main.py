import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

requirement = input("Describe the Python program you need: ")

prompt = f"""
You are an experienced Python developer.

Write a Python program for the following requirement.

Requirement:
{requirement}

Rules:
- Generate only Python code.
- Include comments.
- Keep the solution beginner-friendly.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)

print("\nGenerated Python Code")
print("-" * 60)
print(response.choices[0].message.content)
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

topic = input("Topic: ")
audience = input("Target Audience: ")
tone = input("Tone (Formal/Friendly): ")
length = input("Length (Short/Medium/Long): ")

prompt = f"""
You are an expert instructor.

Topic:
{topic}

Audience:
{audience}

Tone:
{tone}

Length:
{length}

Explain the topic clearly.

Include:
1. Definition
2. Benefits
3. Example
4. Summary
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.4
)

print("\nGenerated Response")
print("-" * 50)
print(response.choices[0].message.content)
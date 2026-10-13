import os
import json
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

Return ONLY valid JSON.

Structure:

{{
    "title": "",
    "definition": "",
    "advantages": [],
    "example": "",
    "summary": ""
}}

Do not include markdown.
Do not include explanations.
Return only JSON.
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

content = response.choices[0].message.content

print("\nRaw Response")
print("=" * 60)
print(content)

try:
    data = json.loads(content)

    print("\nParsed Data")
    print("=" * 60)
    print("Title:", data["title"])
    print("Definition:", data["definition"])

    print("\nAdvantages:")
    for item in data["advantages"]:
        print("-", item)

    print("\nExample:", data["example"])
    print("\nSummary:", data["summary"])

except json.JSONDecodeError:
    print("Invalid JSON returned.")
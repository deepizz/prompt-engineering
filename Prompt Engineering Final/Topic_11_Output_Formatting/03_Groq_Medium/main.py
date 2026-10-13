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

Return ONLY valid JSON using this structure.

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

print("\nGenerated JSON")
print("-" * 50)

content = response.choices[0].message.content
print(content)

# Parse JSON
try:
    data = json.loads(content)

    print("\nParsed JSON")
    print("-" * 50)
    print("Title:", data["title"])
    print("Definition:", data["definition"])
    print("Advantages:", data["advantages"])
    print("Example:", data["example"])
    print("Summary:", data["summary"])

except json.JSONDecodeError:
    print("\nThe response was not valid JSON.")
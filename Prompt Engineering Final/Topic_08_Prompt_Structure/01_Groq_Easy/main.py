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
ROLE:
You are an experienced teacher.

TASK:
Explain the given topic.

CONTEXT:
The audience is a beginner learning AI.

CONSTRAINTS:
- Maximum 150 words
- Use simple English
- Include one real-world example

OUTPUT FORMAT:
- Definition
- Example
- Summary

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

print("\nGenerated Response")
print("-" * 50)
print(response.choices[0].message.content)
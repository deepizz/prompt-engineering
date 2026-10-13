import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

weak_prompt = input("Enter a weak prompt: ")

prompt = f"""
You are an expert Prompt Engineer.

Your task is to improve the following prompt.

Weak Prompt:
{weak_prompt}

Improve it by:
- Making it clear
- Adding necessary details
- Specifying the expected output
- Keeping it concise

Return only the improved prompt.
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

print("\nImproved Prompt")
print("-" * 50)
print(response.choices[0].message.content)
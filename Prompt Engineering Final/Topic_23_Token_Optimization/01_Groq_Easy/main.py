import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

long_prompt = input("Enter a long prompt:\n")

optimizer_prompt = f"""
You are a prompt optimization expert.

Rewrite the following prompt.

Requirements:
- Keep the same meaning.
- Remove unnecessary words.
- Make it concise.
- Preserve all important instructions.

Prompt:
{long_prompt}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": optimizer_prompt
        }
    ],
    temperature=0.2
)

print("\nOptimized Prompt")
print("-" * 50)
print(response.choices[0].message.content)
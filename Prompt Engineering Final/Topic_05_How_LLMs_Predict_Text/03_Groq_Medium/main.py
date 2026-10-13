import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

text = input("Start a sentence: ")

prompt = f"""
Continue the following sentence naturally.

Sentence:
{text}

Only continue the sentence.
Do not repeat the original text.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3,
    max_tokens=40
)

print("\nPredicted Continuation")
print("-" * 40)
print(response.choices[0].message.content)
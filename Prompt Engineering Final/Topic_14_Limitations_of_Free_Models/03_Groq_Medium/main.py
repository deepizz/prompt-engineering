import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

prompt = """
Write about Artificial Intelligence.

Follow ALL these instructions:

1. Maximum 120 words.
2. Include exactly 5 bullet points.
3. Mention one real-world example.
4. End with the sentence:
   AI is transforming the future.
5. Do not use the word "technology".
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
print("-" * 60)
print(response.choices[0].message.content)
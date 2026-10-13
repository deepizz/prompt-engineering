import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

question = input("Enter your question: ")

prompt = f"""
Question:
{question}

Follow these steps:

Step 1:
Write an initial answer.

Step 2:
Review your answer and identify any weaknesses or missing information.

Step 3:
Rewrite the answer with the improvements.

Clearly label each step.
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

print("\nSelf-Reflection Output")
print("-" * 50)
print(response.choices[0].message.content)
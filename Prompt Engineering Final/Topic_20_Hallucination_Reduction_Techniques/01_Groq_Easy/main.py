import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

context = """
Python was created by Guido van Rossum.
The first public release of Python was in 1991.
Python is an interpreted programming language.
"""

question = input("Ask a question about Python: ")

prompt = f"""
You are a factual assistant.

Use ONLY the information in the context below.

Context:
{context}

Question:
{question}

Rules:
- Do not guess.
- Do not use outside knowledge.
- If the answer is not in the context, reply:
'I don't have enough information from the provided context.'
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.1
)

print("\nAI Response")
print("-" * 50)
print(response.choices[0].message.content)
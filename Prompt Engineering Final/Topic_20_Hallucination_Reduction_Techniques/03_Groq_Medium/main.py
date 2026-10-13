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
Python first appeared in 1991.
Python supports object-oriented programming.
"""

question = input("Ask a question: ")

prompt = f"""
You are a careful AI assistant.

Context:
{context}

Question:
{question}

Instructions:

Step 1:
Find the facts in the context that are relevant.

Step 2:
Determine whether those facts fully answer the question.

Step 3:
If yes, answer using only those facts.

Step 4:
If no, reply:
'I don't have enough information from the provided context.'

Output Format:

Relevant Facts:
...

Answer:
...
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

print(response.choices[0].message.content)
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# -------------------------------
# Knowledge Base
# -------------------------------
knowledge_base = {
    "annual leave": "Employees receive 24 days of annual leave every year.",
    "work from home": "Employees may work from home up to 3 days each week.",
    "medical insurance": "Medical insurance covers employees and their immediate family.",
    "office timing": "Office hours are from 9 AM to 6 PM."
}

# -------------------------------
# User Question
# -------------------------------
question = input("Ask your HR question: ")

# -------------------------------
# Step 1 : Retrieval
# -------------------------------
context = "No relevant information found."

for keyword, information in knowledge_base.items():
    if keyword.lower() in question.lower():
        context = information
        break

# -------------------------------
# Step 2 : Prompt Augmentation
# -------------------------------
prompt = f"""
You are an HR Assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

If the answer is not available in the context,
reply:

I don't have enough information.
"""

# -------------------------------
# Step 3 : Generation
# -------------------------------
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

print("\nRetrieved Context")
print("-" * 50)
print(context)

print("\nAI Response")
print("-" * 50)
print(response.choices[0].message.content)
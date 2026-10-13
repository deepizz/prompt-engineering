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
# Load Knowledge Base
# -------------------------------
with open("knowledge.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()

# -------------------------------
# User Question
# -------------------------------
question = input("Ask your HR question: ")

# -------------------------------
# Step 1 : Retrieval
# -------------------------------
paragraphs = knowledge.split("\n\n")

context = "No relevant information found."

question_words = question.lower().split()

for paragraph in paragraphs:

    if any(word in paragraph.lower() for word in question_words):
        context = paragraph
        break

# -------------------------------
# Step 2 : Prompt Augmentation
# -------------------------------
prompt = f"""
You are an HR Assistant.

Use ONLY the following context.

Context:
{context}

Question:
{question}

If the answer is unavailable, reply:

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
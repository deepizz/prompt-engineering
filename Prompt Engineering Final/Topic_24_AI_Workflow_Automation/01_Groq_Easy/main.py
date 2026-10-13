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

# -----------------------------
# Step 1 - Explain
# -----------------------------
explanation = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Explain {topic} for beginners."
        }
    ],
    temperature=0.2
).choices[0].message.content

# -----------------------------
# Step 2 - Summarize
# -----------------------------
summary = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Summarize this into five bullet points:\n\n{explanation}"
        }
    ],
    temperature=0.2
).choices[0].message.content

# -----------------------------
# Step 3 - Quiz
# -----------------------------
quiz = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Create five quiz questions based on:\n\n{summary}"
        }
    ],
    temperature=0.3
).choices[0].message.content

print("\nExplanation")
print("=" * 60)
print(explanation)

print("\nSummary")
print("=" * 60)
print(summary)

print("\nQuiz")
print("=" * 60)
print(quiz)
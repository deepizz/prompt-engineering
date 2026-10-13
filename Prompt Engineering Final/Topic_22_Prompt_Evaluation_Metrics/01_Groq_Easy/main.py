import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

question = input("Enter a question: ")

# -----------------------------
# Step 1: Generate Response
# -----------------------------
answer = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0.3
).choices[0].message.content

print("\nGenerated Answer")
print("=" * 60)
print(answer)

# -----------------------------
# Step 2: Evaluate Response
# -----------------------------
evaluation_prompt = f"""
You are an AI evaluator.

Evaluate the following answer.

Question:
{question}

Answer:
{answer}

Score each category from 1 to 10.

Return the result in this format:

Accuracy:
Completeness:
Clarity:
Relevance:
Instruction Following:

Overall Feedback:
"""

evaluation = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": evaluation_prompt
        }
    ],
    temperature=0.2
).choices[0].message.content

print("\nEvaluation")
print("=" * 60)
print(evaluation)
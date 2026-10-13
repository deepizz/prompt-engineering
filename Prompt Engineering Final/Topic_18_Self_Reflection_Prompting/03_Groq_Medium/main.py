import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

question = input("Enter your question: ")

# ----------------------------------
# Step 1: Generate
# ----------------------------------
generate_prompt = f"""
Answer the following question.

Question:
{question}
"""

initial_answer = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": generate_prompt
        }
    ]
).choices[0].message.content

print("\nInitial Answer")
print("=" * 60)
print(initial_answer)

# ----------------------------------
# Step 2: Review
# ----------------------------------
review_prompt = f"""
Review the following answer.

Identify:
- Missing information
- Incorrect statements
- Areas for improvement

Answer:
{initial_answer}
"""

review = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": review_prompt
        }
    ]
).choices[0].message.content

print("\nReview")
print("=" * 60)
print(review)

# ----------------------------------
# Step 3: Improve
# ----------------------------------
improve_prompt = f"""
Improve the answer using the review below.

Original Answer:
{initial_answer}

Review:
{review}

Produce the best possible final answer.
"""

final_answer = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": improve_prompt
        }
    ]
).choices[0].message.content

print("\nImproved Answer")
print("=" * 60)
print(final_answer)
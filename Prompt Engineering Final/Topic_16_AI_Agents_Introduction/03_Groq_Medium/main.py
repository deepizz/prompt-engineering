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
# Agent 1 : Research Agent
# -----------------------------
research_prompt = f"""
You are a Research Agent.

Research the following topic and provide detailed information.

Topic:
{topic}
"""

research = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": research_prompt
        }
    ]
).choices[0].message.content

print("\nResearch Agent Output")
print("=" * 60)
print(research)

# -----------------------------
# Agent 2 : Summary Agent
# -----------------------------
summary_prompt = f"""
You are a Summary Agent.

Summarize the following content in five bullet points.

Content:
{research}
"""

summary = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": summary_prompt
        }
    ]
).choices[0].message.content

print("\nSummary Agent Output")
print("=" * 60)
print(summary)

# -----------------------------
# Agent 3 : Reviewer Agent
# -----------------------------
review_prompt = f"""
You are a Reviewer Agent.

Review the following summary.

Check:
- Accuracy
- Clarity
- Completeness

Provide suggestions for improvement.

Summary:
{summary}
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

print("\nReviewer Agent Output")
print("=" * 60)
print(review)
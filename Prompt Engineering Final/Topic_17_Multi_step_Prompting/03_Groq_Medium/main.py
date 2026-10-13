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

# ----------------------------------
# Step 1: Research
# ----------------------------------
research_prompt = f"""
Research the following topic.

Topic:
{topic}

Provide detailed information.
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

print("\nResearch")
print("=" * 60)
print(research)

# ----------------------------------
# Step 2: Summarize
# ----------------------------------
summary_prompt = f"""
Summarize the following information in five bullet points.

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

print("\nSummary")
print("=" * 60)
print(summary)

# ----------------------------------
# Step 3: Quiz Generation
# ----------------------------------
quiz_prompt = f"""
Create five interview questions based on the following summary.

Summary:
{summary}
"""

quiz = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": quiz_prompt
        }
    ]
).choices[0].message.content

print("\nInterview Questions")
print("=" * 60)
print(quiz)
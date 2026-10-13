import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

role = input("Role: ")
task = input("Task: ")
context = input("Context: ")
constraints = input("Constraints: ")
output_format = input("Output Format: ")

prompt = f"""
ROLE:
{role}

TASK:
{task}

CONTEXT:
{context}

CONSTRAINTS:
{constraints}

OUTPUT FORMAT:
{output_format}
"""

print("\nGenerated Prompt")
print("=" * 60)
print(prompt)

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

print("\nAI Response")
print("=" * 60)
print(response.choices[0].message.content)
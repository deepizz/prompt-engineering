import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

problem = input("Enter a problem: ")

prompt = f"""
Solve the following problem step by step.

Problem:
{problem}

Follow these steps:

Step 1:
Understand the problem.

Step 2:
Provide the solution.

Step 3:
Explain why the solution works.

Step 4:
Give a simple example.
"""

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

print("\nStep-by-Step Solution")
print("-" * 50)
print(response.choices[0].message.content)
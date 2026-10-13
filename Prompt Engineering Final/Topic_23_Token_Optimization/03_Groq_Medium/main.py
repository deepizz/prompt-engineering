import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

long_prompt = input("Enter a long prompt:\n")

# ----------------------------------
# Step 1: Optimize Prompt
# ----------------------------------
optimization_prompt = f"""
Rewrite the following prompt.

Requirements:
- Preserve the meaning.
- Reduce unnecessary words.
- Keep all important instructions.

Prompt:
{long_prompt}

Return only the optimized prompt.
"""

optimized_prompt = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": optimization_prompt
        }
    ]
).choices[0].message.content

# ----------------------------------
# Step 2: Execute Original Prompt
# ----------------------------------
response_original = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": long_prompt
        }
    ]
).choices[0].message.content

# ----------------------------------
# Step 3: Execute Optimized Prompt
# ----------------------------------
response_optimized = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": optimized_prompt
        }
    ]
).choices[0].message.content

# ----------------------------------
# Display Results
# ----------------------------------
print("\nOriginal Prompt")
print("=" * 60)
print(long_prompt)

print("\nOptimized Prompt")
print("=" * 60)
print(optimized_prompt)

print("\nResponse to Original Prompt")
print("=" * 60)
print(response_original)

print("\nResponse to Optimized Prompt")
print("=" * 60)
print(response_optimized)
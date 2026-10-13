import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

weak_prompt = input("Enter a prompt: ")

# ----------------------------------
# Step 1: Optimize the Prompt
# ----------------------------------
optimizer_prompt = f"""
You are an expert Prompt Engineer.

Improve the following prompt.

Prompt:
{weak_prompt}

Requirements:
- Make it more specific.
- Add context if needed.
- Specify the output format.
- Keep it concise.

Return only the improved prompt.
"""

optimized_prompt = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": optimizer_prompt
        }
    ]
).choices[0].message.content

# ----------------------------------
# Step 2: Run Original Prompt
# ----------------------------------
original_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": weak_prompt
        }
    ]
).choices[0].message.content

# ----------------------------------
# Step 3: Run Optimized Prompt
# ----------------------------------
optimized_response = client.chat.completions.create(
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
print(weak_prompt)

print("\nOptimized Prompt")
print("=" * 60)
print(optimized_prompt)

print("\nResponse to Original Prompt")
print("=" * 60)
print(original_response)

print("\nResponse to Optimized Prompt")
print("=" * 60)
print(optimized_response)
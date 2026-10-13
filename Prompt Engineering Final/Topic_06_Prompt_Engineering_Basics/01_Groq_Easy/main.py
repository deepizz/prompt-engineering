import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Prompt Engineering Demo")
print("1. Basic Prompt")
print("2. Detailed Prompt")

choice = input("\nChoose (1 or 2): ")

if choice == "1":
    prompt = "Explain Python."

elif choice == "2":
    prompt = """
You are an experienced Python instructor.

Explain Python for beginners.

Requirements:
- Keep it under 150 words.
- Explain what Python is.
- Mention two real-world applications.
- Give one simple example.
- Use bullet points.
"""

else:
    print("Invalid choice.")
    exit()

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

print("\nResponse")
print("-" * 50)
print(response.choices[0].message.content)
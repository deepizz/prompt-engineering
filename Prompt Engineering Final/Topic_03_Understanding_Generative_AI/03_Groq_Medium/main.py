import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Content Types")
print("1. Email")
print("2. Blog")
print("3. Product Description")
print("4. Social Media Post")

choice = input("\nChoose an option (1-4): ")
topic = input("Enter the topic: ")

content_types = {
    "1": "Write a professional email.",
    "2": "Write a blog article.",
    "3": "Write an attractive product description.",
    "4": "Write a social media post."
}

instruction = content_types.get(choice)

if instruction is None:
    print("Invalid choice.")
    exit()

prompt = f"""
{instruction}

Topic:
{topic}

Requirements:
- Clear and engaging
- Well structured
- Professional tone
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)

print("\nGenerated Content")
print("-" * 50)
print(response.choices[0].message.content)
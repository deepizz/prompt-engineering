import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Prompt Complexity Demo")
print("1. Simple Prompt")
print("2. Complex Prompt")

choice = input("\nChoose (1-2): ")

if choice == "1":

    prompt = """
Explain what Python is.
"""

elif choice == "2":

    prompt = """
You are an expert software instructor.

Explain Python in detail.

Requirements:
- Definition
- History
- Features
- Advantages
- Disadvantages
- Data Types
- Control Statements
- Functions
- OOP Concepts
- File Handling
- Exception Handling
- Libraries
- Real-world Applications
- Career Opportunities
- Interview Questions
- Best Practices

Format the response using headings and bullet points.
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
print("-" * 60)
print(response.choices[0].message.content)
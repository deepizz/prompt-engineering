import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Output Formats")
print("1. Paragraph")
print("2. Bullet Points")
print("3. Numbered List")
print("4. Markdown")

choice = input("\nChoose a format (1-4): ")

topic = input("Enter a topic: ")

formats = {
    "1": "Return the response as a paragraph.",
    "2": "Return the response as bullet points.",
    "3": "Return the response as a numbered list.",
    "4": "Return the response in Markdown format with headings."
}

instruction = formats.get(choice)

if instruction is None:
    print("Invalid choice.")
    exit()

prompt = f"""
Explain the following topic.

Topic:
{topic}

Output Format:
{instruction}
"""

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

print("\nGenerated Response")
print("-" * 50)
print(response.choices[0].message.content)
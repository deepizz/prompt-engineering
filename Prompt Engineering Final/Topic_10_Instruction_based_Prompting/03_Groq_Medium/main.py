import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

topic = input("Topic: ")
target = input("Target Audience: ")
word_limit = input("Maximum Words: ")
tone = input("Tone (Formal/Friendly): ")
example = input("Include Example? (yes/no): ")

instructions = f"""
Explain the topic.

Topic:
{topic}

Instructions:
- Audience: {target}
- Tone: {tone}
- Maximum {word_limit} words.
"""

if example.lower() == "yes":
    instructions += "\n- Include one practical example."

instructions += "\n- End with three key takeaways."

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": instructions
        }
    ],
    temperature=0.3
)

print("\nPrompt Sent to the Model")
print("=" * 60)
print(instructions)

print("\nAI Response")
print("=" * 60)
print(response.choices[0].message.content)
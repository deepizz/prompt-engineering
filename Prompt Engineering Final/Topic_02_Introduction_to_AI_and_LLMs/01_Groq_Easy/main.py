import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# User Input
question = input("Ask anything: ")

# Send request to the LLM
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0.3
)

print("\nAI Response")
print("-" * 40)
print(response.choices[0].message.content)
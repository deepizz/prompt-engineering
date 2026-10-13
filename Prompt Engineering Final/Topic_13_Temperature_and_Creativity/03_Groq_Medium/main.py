import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("AI Writing Assistant")
print("1. Explain a Topic")
print("2. Write a Story")
print("3. Generate Python Code")
print("4. Brainstorm Ideas")

choice = input("\nChoose an option (1-4): ")
topic = input("Enter the topic: ")

tasks = {
    "1": {
        "prompt": f"Explain {topic} in simple terms.",
        "temperature": 0.2
    },
    "2": {
        "prompt": f"Write a creative story about {topic}.",
        "temperature": 1.0
    },
    "3": {
        "prompt": f"Write a Python program for {topic}.",
        "temperature": 0.1
    },
    "4": {
        "prompt": f"Generate 10 creative ideas about {topic}.",
        "temperature": 0.9
    }
}

task = tasks.get(choice)

if task is None:
    print("Invalid choice.")
    exit()

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": task["prompt"]
        }
    ],
    temperature=task["temperature"]
)

print("\nTemperature Used:", task["temperature"])
print("-" * 50)
print(response.choices[0].message.content)
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

topic = input("Enter a topic: ")

temperatures = [0.2, 1.0]

for temp in temperatures:

    print("\n" + "=" * 60)
    print(f"Temperature: {temp}")
    print("=" * 60)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"Write a short paragraph about {topic}."
            }
        ],
        temperature=temp
    )

    print(response.choices[0].message.content)
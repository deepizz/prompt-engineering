import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Prompt Types")
print("1. Zero-Shot")
print("2. One-Shot")
print("3. Few-Shot")

choice = input("\nChoose (1-3): ")

if choice == "1":

    prompt = """
Classify the sentiment of the following sentence.

Sentence:
I absolutely love this phone.
"""

elif choice == "2":

    prompt = """
Example:

Sentence: This movie was amazing.
Sentiment: Positive

Now classify.

Sentence:
I absolutely love this phone.
"""

elif choice == "3":

    prompt = """
Examples

Sentence: This movie was amazing.
Sentiment: Positive

Sentence: The food was terrible.
Sentiment: Negative

Sentence: The product is okay.
Sentiment: Neutral

Now classify.

Sentence:
I absolutely love this phone.
"""

else:
    print("Invalid Choice")
    exit()

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)

print("\nResult")
print("-" * 40)
print(response.choices[0].message.content)
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

sentence = input("Enter a sentence: ")

prompts = {
    "Zero-Shot": f"""
Classify the sentiment.

Sentence:
{sentence}
""",

    "One-Shot": f"""
Example

Sentence: I enjoy learning AI.
Sentiment: Positive

Now classify.

Sentence:
{sentence}
""",

    "Few-Shot": f"""
Examples

Sentence: I enjoy learning AI.
Sentiment: Positive

Sentence: This laptop is horrible.
Sentiment: Negative

Sentence: The meeting was okay.
Sentiment: Neutral

Now classify.

Sentence:
{sentence}
"""
}

for prompt_type, prompt in prompts.items():

    print(f"\n{'='*50}")
    print(prompt_type)
    print("="*50)

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

    print(response.choices[0].message.content)
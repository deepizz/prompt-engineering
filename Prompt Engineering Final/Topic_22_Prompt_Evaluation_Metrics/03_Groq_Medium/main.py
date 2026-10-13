import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

question = input("Enter a topic: ")

prompt_a = f"""
Explain {question}.
"""

prompt_b = f"""
You are an experienced instructor.

Explain {question} for beginners.

Requirements:
- Maximum 200 words
- Include one example
- End with three key takeaways
"""

# -----------------------------
# Response A
# -----------------------------
response_a = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt_a}]
).choices[0].message.content

# -----------------------------
# Response B
# -----------------------------
response_b = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt_b}]
).choices[0].message.content

print("\nPrompt A Response")
print("=" * 60)
print(response_a)

print("\nPrompt B Response")
print("=" * 60)
print(response_b)

# -----------------------------
# Compare Both Responses
# -----------------------------
judge_prompt = f"""
You are an AI evaluator.

Compare these two responses.

Question:
{question}

Response A:
{response_a}

Response B:
{response_b}

Evaluate using:

- Accuracy
- Completeness
- Clarity
- Relevance
- Instruction Following

Choose the better response.

Return ONLY valid JSON.

{{
    "winner": "",
    "scores": {{
        "response_a": {{
            "accuracy": 0,
            "completeness": 0,
            "clarity": 0,
            "relevance": 0,
            "instruction_following": 0
        }},
        "response_b": {{
            "accuracy": 0,
            "completeness": 0,
            "clarity": 0,
            "relevance": 0,
            "instruction_following": 0
        }}
    }},
    "reason": ""
}}
"""

evaluation = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": judge_prompt
        }
    ],
    temperature=0
).choices[0].message.content

print("\nEvaluation Result")
print("=" * 60)
print(evaluation)
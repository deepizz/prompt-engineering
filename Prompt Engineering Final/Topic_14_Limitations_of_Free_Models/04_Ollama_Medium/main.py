import ollama

question = input("Enter your question: ")

# ------------------------------------
# Step 1 - Generate an Answer
# ------------------------------------

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

answer = response["message"]["content"]

print("\nGenerated Answer")
print("=" * 60)
print(answer)

# ------------------------------------
# Step 2 - Evaluate the Answer
# ------------------------------------

evaluation_prompt = f"""
You are an AI evaluator.

Review the following answer.

Question:
{question}

Answer:
{answer}

Identify the following:

## Strengths
- What did the answer do well?

## Limitations
- Was anything missing?
- Were there assumptions?
- Could the answer become outdated?

## Confidence
High / Medium / Low

## Recommendation
Should the user verify this information using trusted sources?
Explain why.
"""

evaluation = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": evaluation_prompt
        }
    ]
)

print("\nEvaluation")
print("=" * 60)
print(evaluation["message"]["content"])
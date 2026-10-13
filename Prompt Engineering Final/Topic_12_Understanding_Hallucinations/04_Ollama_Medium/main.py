import ollama

question = input("Enter your question: ")

# -------------------------------------
# Step 1: Generate an Answer
# -------------------------------------

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""
Answer the following question.

Question:
{question}
"""
        }
    ]
)

answer = response["message"]["content"]

print("\nGenerated Answer")
print("=" * 60)
print(answer)

# -------------------------------------
# Step 2: Self Review
# -------------------------------------

review_prompt = f"""
You are an AI fact checker.

Review the following answer.

Question:
{question}

Answer:
{answer}

Evaluate the answer using the following sections:

## Confidence Level
(High / Medium / Low)

## Possible Hallucination
(State whether any claim appears uncertain.)

## Recommendation
(Explain whether the user should verify this information from a trusted source.)

Keep the review concise.
"""

review = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": review_prompt
        }
    ]
)

print("\nFact Check")
print("=" * 60)
print(review["message"]["content"])
import ollama

question = input("Enter your question: ")

# -----------------------------------
# Step 1 - Generate Response
# -----------------------------------

answer_prompt = f"""
You are a helpful AI assistant.

Answer the following question clearly and concisely.

Question:
{question}
"""

answer = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": answer_prompt
        }
    ]
)["message"]["content"]

print("\nGenerated Response")
print("=" * 60)
print(answer)

# -----------------------------------
# Step 2 - Evaluate Response
# -----------------------------------

evaluation_prompt = f"""
You are an AI evaluator.

Evaluate the following response.

Question:
{question}

Response:
{answer}

Score each category from 1 to 10.

Evaluation Criteria:

1. Accuracy
2. Clarity
3. Completeness
4. Relevance
5. Conciseness

Finally provide:

- Overall Score (out of 10)
- One strength
- One improvement suggestion

OUTPUT FORMAT:

## Evaluation

Accuracy:
Clarity:
Completeness:
Relevance:
Conciseness:

Overall Score:

Strength:

Improvement:
"""

evaluation = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": evaluation_prompt
        }
    ]
)["message"]["content"]

print("\nPrompt Evaluation")
print("=" * 60)
print(evaluation)
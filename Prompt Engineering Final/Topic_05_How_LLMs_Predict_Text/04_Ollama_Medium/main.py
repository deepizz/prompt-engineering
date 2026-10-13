import ollama

text = input("Enter an incomplete sentence: ")

prompt = f"""
You are demonstrating how Large Language Models predict text.

Given the incomplete sentence below:

{text}

TASK:
1. Predict the most likely continuation.
2. Complete the sentence naturally.
3. Explain in 2-3 sentences why this continuation is likely.

OUTPUT FORMAT:

## Predicted Continuation

## Explanation
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nNext Word Prediction Demo")
print("=" * 60)
print(response["message"]["content"])
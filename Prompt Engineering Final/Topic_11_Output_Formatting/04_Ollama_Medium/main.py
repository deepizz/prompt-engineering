import ollama

review = input("Enter a product review:\n")

prompt = f"""
ROLE:
You are a Product Review Analyst.

TASK:
Analyze the following customer review.

CUSTOMER REVIEW:
{review}

INSTRUCTIONS:
1. Identify the overall sentiment.
2. List the positive points.
3. List the negative points.
4. Give an overall rating out of 5.
5. Suggest one improvement for the product.

OUTPUT FORMAT:

# Review Analysis

## Overall Sentiment

## Positive Points
- Point 1
- Point 2

## Negative Points
- Point 1
- Point 2

## Rating

## Suggested Improvement
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

print("\nReview Analysis")
print("=" * 60)
print(response["message"]["content"])
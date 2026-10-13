import ollama

topic = input("Enter an essay topic: ")

# -----------------------------------
# Step 1 - Generate Essay
# -----------------------------------

essay_prompt = f"""
You are an experienced content writer.

Write a short essay (200-250 words) on:

{topic}
"""

essay = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": essay_prompt
        }
    ]
)["message"]["content"]

print("\nGenerated Essay")
print("=" * 60)
print(essay)

# -----------------------------------
# Step 2 - Self Reflection
# -----------------------------------

review_prompt = f"""
You are a senior editor.

Review the following essay.

Essay:

{essay}

Evaluate the essay based on:

1. Clarity
2. Grammar
3. Organization
4. Completeness
5. Suggestions for improvement

Do not rewrite the essay.

Provide constructive feedback.
"""

review = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": review_prompt
        }
    ]
)["message"]["content"]

print("\nReview")
print("=" * 60)
print(review)

# -----------------------------------
# Step 3 - Improve Essay
# -----------------------------------

improve_prompt = f"""
Improve the following essay using the review below.

Essay:

{essay}

Review:

{review}

Return only the improved essay.
"""

improved = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": improve_prompt
        }
    ]
)["message"]["content"]

print("\nImproved Essay")
print("=" * 60)
print(improved)
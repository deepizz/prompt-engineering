import ollama

user_prompt = input("Enter your prompt: ")

# -----------------------------------
# Step 1 - Optimize the Prompt
# -----------------------------------

optimizer_prompt = f"""
You are an expert Prompt Engineer.

Improve the following prompt.

Original Prompt:
{user_prompt}

Your job is to:
1. Make the prompt more specific.
2. Add missing context if appropriate.
3. Add clear instructions.
4. Specify the expected output format.
5. Keep the user's original intent unchanged.

Return ONLY the optimized prompt.
"""

optimized_prompt = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": optimizer_prompt
        }
    ]
)["message"]["content"]

print("\nOptimized Prompt")
print("=" * 60)
print(optimized_prompt)

# -----------------------------------
# Step 2 - Execute the Optimized Prompt
# -----------------------------------

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": optimized_prompt
        }
    ]
)["message"]["content"]

print("\nAI Response")
print("=" * 60)
print(response)
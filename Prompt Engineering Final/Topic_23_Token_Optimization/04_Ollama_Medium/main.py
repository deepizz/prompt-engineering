import ollama

topic = input("Enter a topic: ")

# -----------------------------------
# Verbose Prompt
# -----------------------------------

verbose_prompt = f"""
You are a highly experienced university professor with more than
25 years of teaching experience.

Please explain the following topic in great detail.

The explanation should include:
- Definition
- History
- Advantages
- Disadvantages
- Applications
- Real-world examples
- Future scope
- Conclusion

Topic:
{topic}
"""

# -----------------------------------
# Optimized Prompt
# -----------------------------------

optimized_prompt = f"""
Explain the following topic for beginners.

Topic:
{topic}

Include:
- Definition
- Applications
- One real-world example

Limit the response to 200 words.
"""

# -----------------------------------
# Function
# -----------------------------------

def ask_model(prompt):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

# -----------------------------------
# Execute
# -----------------------------------

verbose_answer = ask_model(verbose_prompt)
optimized_answer = ask_model(optimized_prompt)

# -----------------------------------
# Display Results
# -----------------------------------

print("\n" + "=" * 70)
print("VERBOSE PROMPT")
print("=" * 70)
print(verbose_answer)

print("\nApproximate Prompt Length:",
      len(verbose_prompt.split()), "words")

print("\n" + "=" * 70)
print("OPTIMIZED PROMPT")
print("=" * 70)
print(optimized_answer)

print("\nApproximate Prompt Length:",
      len(optimized_prompt.split()), "words")
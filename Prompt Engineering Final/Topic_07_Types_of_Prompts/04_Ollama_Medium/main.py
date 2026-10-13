import ollama

topic = input("Enter a topic: ")

prompt_types = {
    "Zero-Shot Prompt": f"""
Explain the following topic:

{topic}
""",

    "Few-Shot Prompt": f"""
Example 1

Topic: Python

Explanation:
Python is a beginner-friendly programming language used in web development,
data science, AI, and automation.

--------------------------------

Now explain:

Topic:
{topic}
""",

    "Role Prompt": f"""
You are an experienced university professor.

Teach the following topic to first-year engineering students.

Topic:
{topic}
""",

    "Instruction Prompt": f"""
Explain the following topic.

Topic:
{topic}

Instructions:
- Use simple language.
- Keep it under 200 words.
- Give one real-world example.
- End with three key takeaways.
"""
}

for title, prompt in prompt_types.items():

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(response["message"]["content"])
import ollama

print("Enter your Python code (type END on a new line to finish):")

lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

code = "\n".join(lines)

prompt = f"""
ROLE:
You are an experienced Senior Python Developer.

TASK:
Review the Python code provided below.

CODE:
{code}

INSTRUCTIONS:
1. Explain what the code does.
2. Identify any issues or bad practices.
3. Suggest improvements.
4. Rewrite the code following Python best practices.
5. Add comments to the improved code.

OUTPUT FORMAT:

## Code Explanation

## Issues Found

## Suggested Improvements

## Improved Code
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

print("\nAI Code Review")
print("=" * 60)
print(response["message"]["content"])
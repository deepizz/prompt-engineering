import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("Paste your Python code below.")
print("Type END on a new line when finished.\n")

lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

code = "\n".join(lines)

prompt = f"""
You are a senior Python code reviewer.

Analyze the following code.

Tasks:
1. Explain what the code does.
2. Identify bugs or potential issues.
3. Suggest improvements.
4. Provide an improved version of the code.

Return the answer using these headings:

## Explanation

## Issues

## Improved Code

Code:
```python
{code}
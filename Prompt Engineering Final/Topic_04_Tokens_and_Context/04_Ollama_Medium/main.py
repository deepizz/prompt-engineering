import ollama

document = """
Python is a high-level programming language created by Guido van Rossum.
It was first released in 1991.

Python supports multiple programming paradigms including:
- Object-Oriented Programming
- Functional Programming
- Procedural Programming

Python is widely used in:
- Artificial Intelligence
- Data Science
- Web Development
- Automation
"""

question = input("Ask a question about the document: ")

prompt = f"""
ROLE:
You are a Document Analysis Assistant.

TASK:
Answer the user's question using ONLY the document below.

DOCUMENT:
{document}

QUESTION:
{question}

RULES:
1. Answer only using the document.
2. If the answer is not available, say:
   "The document does not contain that information."
3. Do not guess.

OUTPUT FORMAT:

## Answer

## Supporting Information
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

print("\nDocument Analysis")
print("=" * 60)
print(response["message"]["content"])
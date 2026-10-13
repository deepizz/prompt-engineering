import ollama

context = """
Company HR Policy

- Employees receive 24 days of annual leave.
- Employees may work from home up to 3 days per week.
- Medical insurance covers employees and immediate family members.
- Office working hours are 9:00 AM to 6:00 PM.
"""

question = input("Ask an HR question: ")

prompt = f"""
ROLE:
You are an HR Assistant.

TASK:
Answer the user's question using ONLY the information
provided in the context.

CONTEXT:
{context}

QUESTION:
{question}

RULES:
1. Answer ONLY using the context.
2. If the answer is not available, reply:
   "I don't have enough information in the provided context."
3. Do not make assumptions.
4. Do not use outside knowledge.
5. Quote the relevant information when possible.

OUTPUT FORMAT:

## Answer

## Evidence
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

print("\nHallucination Reduction Demo")
print("=" * 60)
print(response["message"]["content"])
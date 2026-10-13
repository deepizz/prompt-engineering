import ollama

purpose = input("Email Purpose: ")
recipient = input("Recipient: ")
tone = input("Tone (Formal/Friendly/Professional): ")

prompt = f"""
ROLE:
You are an expert Business Communication Specialist.

TASK:
Write a professional email.

DETAILS:
Purpose: {purpose}
Recipient: {recipient}
Tone: {tone}

INSTRUCTIONS:
1. Begin with an appropriate greeting.
2. Write a clear subject line.
3. Keep the email between 150 and 200 words.
4. Use the specified tone throughout.
5. Clearly explain the purpose.
6. End with a professional closing.
7. Do not include placeholders.

OUTPUT FORMAT:

Subject:

Email Body:

Closing:
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

print("\nGenerated Email")
print("=" * 60)
print(response["message"]["content"])
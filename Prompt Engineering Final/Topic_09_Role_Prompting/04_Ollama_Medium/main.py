import ollama

question = input("Enter your question: ")

roles = {
    "Software Engineer": f"""
You are an experienced Software Engineer.

Answer the following question with a technical perspective.

Question:
{question}
""",

    "Teacher": f"""
You are a friendly school teacher.

Explain the following question in simple language that a beginner can understand.

Question:
{question}
""",

    "Business Consultant": f"""
You are a senior Business Consultant.

Answer the following question by focusing on business value,
cost, benefits, and real-world applications.

Question:
{question}
""",

    "Data Scientist": f"""
You are an experienced Data Scientist.

Answer the following question using analytical thinking,
examples, and industry use cases.

Question:
{question}
"""
}

for role, prompt in roles.items():

    print("\n" + "=" * 70)
    print(f"ROLE: {role}")
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
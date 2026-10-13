import ollama

question = input("Ask a question about Artificial Intelligence: ")

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nAI Response")
print("-" * 50)
print(response["message"]["content"])
import ollama

topic = input("Enter a topic: ")

temperatures = [
    (0.0, "Very Low (Highly Deterministic)"),
    (0.3, "Low"),
    (0.7, "Medium"),
    (1.0, "High (More Creative)")
]

for temp, label in temperatures:

    print("\n" + "=" * 70)
    print(f"Temperature: {temp} - {label}")
    print("=" * 70)

    prompt = f"""
You are a creative writing assistant.

Write a short paragraph about:

{topic}

Keep the response under 120 words.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": temp
        }
    )

    print(response["message"]["content"])
import ollama

topic = input("Enter a topic: ")

prompt = f"""
ROLE:
You are an expert Generative AI assistant.

TASK:
Generate educational content for the given topic.

TOPIC:
{topic}

INSTRUCTIONS:

1. Explain the topic.
2. Generate three interesting facts.
3. Generate one real-world use case.
4. Generate a short quiz with three questions.
5. End with a short summary.

OUTPUT FORMAT:

## Explanation

## Interesting Facts

## Real-world Use Case

## Quiz

## Summary
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

print("\nGenerative AI Assistant")
print("=" * 60)
print(response["message"]["content"])
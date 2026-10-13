import ollama

topic = input("Enter an AI topic: ")

prompt = f"""
ROLE:
You are an experienced AI instructor.

TASK:
Teach the given topic to beginners.

TOPIC:
{topic}

INSTRUCTIONS:
1. Explain the topic.
2. List three important concepts.
3. Give one real-world example.
4. Mention one common misconception.
5. End with a short summary.

OUTPUT FORMAT:

## Explanation

## Key Concepts

## Real-world Example

## Common Misconception

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

print("\nAI Learning Assistant")
print("=" * 60)
print(response["message"]["content"])
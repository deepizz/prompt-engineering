import json
import ollama

student_description = input("Enter student details:\n")

prompt = f"""
ROLE:
You are an Information Extraction Assistant.

TASK:
Extract the student's information from the text below.

TEXT:
{student_description}

INSTRUCTIONS:
Extract the following fields:

- name
- age
- course
- university
- skills (array)
- interests (array)

RULES:
1. Return ONLY valid JSON.
2. Do not include markdown.
3. Do not include explanations.
4. If a value is missing, use null.
5. Skills and interests must always be arrays.

Example Output:

{{
  "name": "John Doe",
  "age": 21,
  "course": "Computer Science",
  "university": "ABC University",
  "skills": ["Python", "SQL"],
  "interests": ["AI", "Data Science"]
}}
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

json_text = response["message"]["content"]

print("\nGenerated JSON")
print("=" * 60)
print(json_text)

# -----------------------------------
# Validate JSON
# -----------------------------------

try:
    data = json.loads(json_text)

    print("\nJSON Validation")
    print("=" * 60)
    print("✅ Valid JSON")

    print("\nParsed Object")
    print("=" * 60)

    for key, value in data.items():
        print(f"{key}: {value}")

except json.JSONDecodeError:
    print("\n❌ Invalid JSON returned by the model.")
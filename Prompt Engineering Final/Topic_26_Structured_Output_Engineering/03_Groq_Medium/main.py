import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

student = input("Student Name: ")
subject = input("Subject: ")
marks = int(input("Marks (0-100): "))

prompt = f"""
Create a student performance report.

Student:
{student}

Subject:
{subject}

Marks:
{marks}

Return ONLY valid JSON.

{{
    "student_name": "",
    "subject": "",
    "marks": 0,
    "grade": "",
    "performance": "",
    "recommendations": [
        ""
    ]
}}

Rules:
- Grade A : 90+
- Grade B : 75-89
- Grade C : 60-74
- Grade D : Below 60

Do not return markdown.
Return only JSON.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)

content = response.choices[0].message.content

print("\nRaw JSON")
print("=" * 60)
print(content)

try:
    report = json.loads(content)

    print("\nStudent Report")
    print("=" * 60)
    print("Name :", report["student_name"])
    print("Subject :", report["subject"])
    print("Marks :", report["marks"])
    print("Grade :", report["grade"])
    print("Performance :", report["performance"])

    print("\nRecommendations")
    for item in report["recommendations"]:
        print("-", item)

except json.JSONDecodeError:
    print("Invalid JSON received.")
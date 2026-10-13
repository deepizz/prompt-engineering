import ollama

name = input("Candidate Name: ")
experience = input("Years of Experience: ")
profession = input("Profession: ")
skills = input("Skills (comma separated): ")

prompt = f"""
ROLE:
You are an expert HR Recruiter and Professional Resume Writer.

TASK:
Create a professional resume summary for the candidate.

CONTEXT:

Candidate Name: {name}
Profession: {profession}
Experience: {experience} years
Skills: {skills}

CONSTRAINTS:
- Use professional language.
- Keep the summary under 150 words.
- Highlight the candidate's strengths.
- Mention relevant technical skills.
- Make it ATS-friendly.

OUTPUT FORMAT:

# Professional Summary

# Key Skills

- Skill 1
- Skill 2
- Skill 3
- Skill 4
- Skill 5

# Career Objective
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

print("\nGenerated Resume")
print("=" * 60)
print(response["message"]["content"])
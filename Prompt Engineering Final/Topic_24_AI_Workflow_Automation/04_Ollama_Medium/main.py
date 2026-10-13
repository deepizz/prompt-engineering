import ollama

meeting_notes = input("Enter meeting notes:\n")

# -----------------------------------
# Step 1 - Generate Summary
# -----------------------------------

summary_prompt = f"""
You are a meeting assistant.

Summarize the following meeting notes
in less than 150 words.

Meeting Notes:
{meeting_notes}
"""

summary = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": summary_prompt
        }
    ]
)["message"]["content"]

print("\nMeeting Summary")
print("=" * 60)
print(summary)

# -----------------------------------
# Step 2 - Extract Action Items
# -----------------------------------

action_prompt = f"""
Based on the meeting summary below,
identify all action items.

Meeting Summary:
{summary}

Return them as a numbered list.
"""

actions = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": action_prompt
        }
    ]
)["message"]["content"]

print("\nAction Items")
print("=" * 60)
print(actions)

# -----------------------------------
# Step 3 - Identify Risks
# -----------------------------------

risk_prompt = f"""
Review the meeting summary below.

Meeting Summary:
{summary}

Identify:

- Risks
- Challenges
- Open Questions

Return each as bullet points.
"""

risks = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": risk_prompt
        }
    ]
)["message"]["content"]

print("\nRisks and Open Questions")
print("=" * 60)
print(risks)

# -----------------------------------
# Step 4 - Draft Follow-up Email
# -----------------------------------

email_prompt = f"""
Using the following information:

Meeting Summary:
{summary}

Action Items:
{actions}

Write a professional follow-up email
to all meeting participants.

Include:
- Appreciation
- Summary
- Action Items
- Next Steps
"""

email = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": email_prompt
        }
    ]
)["message"]["content"]

print("\nFollow-up Email")
print("=" * 60)
print(email)
import ollama

industry = input("Enter an industry (e.g., Healthcare, Education, Agriculture): ")

# -----------------------------------
# Step 1 - Generate Business Idea
# -----------------------------------

idea_prompt = f"""
You are a startup consultant.

Suggest one innovative business idea in the following industry:

{industry}

Keep the idea concise.
"""

idea = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": idea_prompt
        }
    ]
)["message"]["content"]

print("\nBusiness Idea")
print("=" * 60)
print(idea)

# -----------------------------------
# Step 2 - Identify Target Customers
# -----------------------------------

customer_prompt = f"""
Based on this business idea:

{idea}

Identify:
- Target customers
- Customer problems
- Value proposition

Return in bullet points.
"""

customers = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": customer_prompt
        }
    ]
)["message"]["content"]

print("\nTarget Customers")
print("=" * 60)
print(customers)

# -----------------------------------
# Step 3 - Create Marketing Strategy
# -----------------------------------

marketing_prompt = f"""
Using the following business idea:

{idea}

Create a simple marketing strategy.

Include:
- Marketing channels
- Pricing approach
- Promotion ideas

Keep it practical.
"""

marketing = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": marketing_prompt
        }
    ]
)["message"]["content"]

print("\nMarketing Strategy")
print("=" * 60)
print(marketing)

# -----------------------------------
# Step 4 - Generate Elevator Pitch
# -----------------------------------

pitch_prompt = f"""
Using the business idea below:

{idea}

Write a 60-second elevator pitch
for investors.

Keep it professional and persuasive.
"""

pitch = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": pitch_prompt
        }
    ]
)["message"]["content"]

print("\nElevator Pitch")
print("=" * 60)
print(pitch)
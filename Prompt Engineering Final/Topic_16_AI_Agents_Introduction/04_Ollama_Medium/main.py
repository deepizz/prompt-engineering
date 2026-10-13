import ollama

goal = input("Enter your learning goal: ")

# -----------------------------------
# Step 1 - Create a Study Plan
# -----------------------------------

plan_prompt = f"""
You are an AI Study Planning Agent.

The user's goal is:

{goal}

Create a learning roadmap with 5 sequential steps.

Return only the roadmap.
"""

plan = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": plan_prompt
        }
    ]
)["message"]["content"]

print("\nLearning Roadmap")
print("=" * 60)
print(plan)

# -----------------------------------
# Step 2 - Recommend Resources
# -----------------------------------

resource_prompt = f"""
Based on this learning roadmap:

{plan}

Recommend:
- Books
- Free online resources
- Practice activities

Keep it concise.
"""

resources = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": resource_prompt
        }
    ]
)["message"]["content"]

print("\nRecommended Resources")
print("=" * 60)
print(resources)

# -----------------------------------
# Step 3 - Generate Weekly Schedule
# -----------------------------------

schedule_prompt = f"""
Using the roadmap below:

{plan}

Create a 4-week study schedule.

Assume the student studies
2 hours per day.

Return a weekly plan.
"""

schedule = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": schedule_prompt
        }
    ]
)["message"]["content"]

print("\n4-Week Study Schedule")
print("=" * 60)
print(schedule)
import ollama

destination = input("Enter your travel destination: ")
days = input("Number of days: ")
budget = input("Budget (Low / Medium / High): ")

prompt = f"""
ROLE:
You are an experienced travel planner.

TASK:
Create a personalized travel itinerary.

USER DETAILS:
Destination: {destination}
Duration: {days} days
Budget: {budget}

INSTRUCTIONS:
1. Create a day-by-day itinerary.
2. Recommend tourist attractions.
3. Suggest local foods to try.
4. Recommend transportation options.
5. Include an estimated daily budget.
6. End with useful travel tips.

OUTPUT FORMAT:

# Travel Plan

## Day-wise Itinerary

## Recommended Foods

## Transportation

## Estimated Budget

## Travel Tips
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

print("\nAI Travel Planner")
print("=" * 60)
print(response["message"]["content"])
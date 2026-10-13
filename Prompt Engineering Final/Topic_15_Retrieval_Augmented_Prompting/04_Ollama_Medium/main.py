import ollama

# -----------------------------------------
# Simple Knowledge Base
# -----------------------------------------

knowledge_base = [
    {
        "topic": "Annual Leave",
        "content": """
Employees are entitled to 24 days of paid annual leave each calendar year.
Unused leave can be carried forward up to 5 days.
"""
    },
    {
        "topic": "Work From Home",
        "content": """
Employees may work from home up to three days per week with manager approval.
"""
    },
    {
        "topic": "Medical Insurance",
        "content": """
The company provides medical insurance for employees and their immediate family members.
"""
    }
]

# -----------------------------------------
# Retrieve Relevant Document
# -----------------------------------------

question = input("Ask an HR question: ").lower()

retrieved_document = None

for doc in knowledge_base:
    if doc["topic"].lower() in question:
        retrieved_document = doc["content"]
        break

if retrieved_document is None:
    retrieved_document = "No relevant document was found."

# -----------------------------------------
# Build RAG Prompt
# -----------------------------------------

prompt = f"""
ROLE:
You are an HR Assistant.

TASK:
Answer the user's question using ONLY the retrieved document.

RETRIEVED DOCUMENT:
{retrieved_document}

QUESTION:
{question}

RULES:
1. Answer only using the retrieved document.
2. If the answer is unavailable, say:
   "The knowledge base does not contain this information."
3. Do not guess.

OUTPUT FORMAT:

## Answer

## Source
Retrieved HR Knowledge Base
"""

# -----------------------------------------
# Generate Response
# -----------------------------------------

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nRetrieved Document")
print("=" * 60)
print(retrieved_document)

print("\nAI Response")
print("=" * 60)
print(response["message"]["content"])
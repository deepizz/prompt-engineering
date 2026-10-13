import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

topic = input("Enter blog topic: ")

# --------------------------------
# Step 1 - Generate Outline
# --------------------------------
outline = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Create a blog outline for '{topic}'."
        }
    ]
).choices[0].message.content

# --------------------------------
# Step 2 - Write Blog
# --------------------------------
blog = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Write a blog using this outline:\n\n{outline}"
        }
    ]
).choices[0].message.content

# --------------------------------
# Step 3 - SEO Title
# --------------------------------
seo_title = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Generate an SEO-friendly title for this blog:\n\n{blog}"
        }
    ]
).choices[0].message.content

# --------------------------------
# Step 4 - Meta Description
# --------------------------------
meta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"Write a 150-character meta description for:\n\n{blog}"
        }
    ]
).choices[0].message.content

print("\nSEO Title")
print("=" * 60)
print(seo_title)

print("\nOutline")
print("=" * 60)
print(outline)

print("\nBlog")
print("=" * 60)
print(blog)

print("\nMeta Description")
print("=" * 60)
print(meta)
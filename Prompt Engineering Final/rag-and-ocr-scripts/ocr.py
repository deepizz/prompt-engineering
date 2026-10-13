import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from paddleocr import PaddleOCR

# ----------------------------------------
# Config
# ----------------------------------------

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.3-70b-versatile"

if not GROQ_API_KEY:
    raise ValueError(
        f"Set GROQ_API_KEY as an environment variable or add it to {BASE_DIR / '.env'} before running."
    )

# ----------------------------------------
# Load OCR Model
# ----------------------------------------

print("=" * 60)
print("Loading PaddleOCR...")
print("=" * 60)

ocr = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    enable_mkldnn=False
)

print("OCR Model Loaded")


# ----------------------------------------
# OCR Function
# ----------------------------------------

def extract_text(image_path):
    result = ocr.predict(image_path)

    lines = []
    for res in result:
        rec_texts = res.get("rec_texts", [])
        for text in rec_texts:
            text = text.strip()
            if text:
                lines.append(text)
    return lines


# ----------------------------------------
# Ask Groq LLM (direct REST call, no openai package)
# ----------------------------------------

def ask_llm(all_lines, question):
    context = "\n".join(all_lines)

    prompt = f"""You are an AI assistant.

Answer ONLY using the extracted text below.

If the answer is not available, say:
"I could not find the answer in the image."

Extracted Text:
{context}

Question:
{question}
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Error from Groq API: {response.status_code} - {response.text}"

    data = response.json()
    return data["choices"][0]["message"]["content"]


# ----------------------------------------
# Main Program
# ----------------------------------------

if __name__ == "__main__":
    image_path = r"C:/Users/kanna/Downloads/Hotel-invoice-example1.png"

    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        exit(1)

    print("\nExtracting text from image...")
    ocr_lines = extract_text(image_path)

    print("\n" + "=" * 60)
    print("Extracted Text")
    print("=" * 60)
    for line in ocr_lines:
        print(line)

    if not ocr_lines:
        print("\nNo text was extracted from the image. Exiting.")
        exit(1)

    print("\n")

    while True:
        question = input("Ask a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = ask_llm(ocr_lines, question)

        print("\n" + "=" * 60)
        print("Answer")
        print("=" * 60)
        print(answer)
        print()
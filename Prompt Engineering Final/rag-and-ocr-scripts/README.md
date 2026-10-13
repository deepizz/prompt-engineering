# RAG + OCR Scripts (No Framework, No Web Server)

Two completely standalone Python scripts:

- **`rag.py`** — point it at a PDF, ask questions about it.
- **`ocr.py`** — point it at an image, PaddleOCR reads its text, ask
  questions about that text.

No FastAPI, no file upload, no LangChain, no vector database. Just a
file path typed into the terminal and a question loop.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

pip install -r requirements.txt

cp .env.example .env
# then edit .env and add your GROQ_API_KEY
```

## Run

You can either pass the file path as a command-line argument
(**recommended on Windows** — pasting into an `input()` prompt can
sometimes misbehave in Windows terminals), or type it when prompted.

```bash
# Option A: pass the path as an argument (recommended)
python rag.py "C:\Users\you\Documents\notes.pdf"

# Option B: type it when prompted
python rag.py
```
```
Path to your PDF file: C:\Users\you\Documents\notes.pdf
Reading and chunking the PDF...
Done. Split into 8 chunks.

Ask questions about the PDF. Type 'exit' to quit.

Your question: What is this document about?
Answer: ...
```

```bash
python ocr.py "C:\Users\you\Pictures\sign.png"
```
```
Running OCR on the image...

Extracted text:
...

Ask questions about the image. Type 'exit' to quit.

Your question: What does the sign say?
Answer: ...
```

## How Each Script Works

**`rag.py`:**
```
extract_text()     -> read the PDF's text with pypdf
chunk_text()        -> split it into ~150-word chunks
get_best_chunks()    -> for a question, count word overlap with each
                        chunk, return the top 3 (no embeddings needed --
                        Groq doesn't offer an embeddings API anyway)
ask_groq()            -> send question + those chunks to Groq, return
                         the answer
```

**`ocr.py`:**
```
extract_text_from_image() -> PaddleOCR reads all text in the image
ask_groq()                  -> send question + that text to Groq,
                               return the answer
```

Both scripts only ever call the LLM in one place (`ask_groq()`), and
both use the same model, set via `MODEL` in `.env`.

## Important: Model Update

`llama-3.3-70b-versatile` was **deprecated by Groq on June 17, 2026**.
If you were using it before, that's why you'd see a 404 /
`model_not_found` error. Both scripts now default to
`openai/gpt-oss-120b`, Groq's recommended replacement. You can change
this anytime via `MODEL` in `.env`.

## Troubleshooting: PaddleOCR on Windows

If `ocr.py` fails with `ImportError: DLL load failed while importing
_pyclipper` (or similar), it's a native Windows dependency issue:

1. **Install the Visual C++ Redistributable (x64)** — fixes the vast
   majority of "DLL load failed" errors for compiled Python packages
   on Windows:
   https://aka.ms/vs/17/release/vc_redist.x64.exe
   Restart your terminal after installing.

2. **Reinstall pyclipper with a prebuilt wheel** (don't pin an old
   version — older pyclipper releases have no prebuilt wheel for
   Python 3.12 and will try to compile from source, which needs a C++
   compiler you probably don't have):
   ```bash
   pip uninstall pyclipper -y
   pip install pyclipper --no-cache-dir
   ```
   Watch the output — it should say "Downloading ...whl", not
   "Building wheel".

3. **Confirm you're running 64-bit Python:**
   ```bash
   python -c "import struct; print(struct.calcsize('P') * 8)"
   ```
   Should print `64`.

4. **Test in isolation** before rerunning `ocr.py`:
   ```bash
   python -c "import pyclipper; print('pyclipper OK')"
   ```

## Notes for Students

- Nothing is stored anywhere — run the script, get answers, done. No
  database, no server, no persistence.
- `rag.py`'s retrieval is intentionally simple (word overlap, not
  semantic search) so the whole idea — *retrieve relevant text, then
  ask the LLM to answer using only that text* — fits on one screen.
- Both scripts follow the exact same shape: extract text once up
  front, then loop asking questions about it. That symmetry is worth
  pointing out — RAG and OCR-QA are really the same pattern with a
  different way of getting the source text.

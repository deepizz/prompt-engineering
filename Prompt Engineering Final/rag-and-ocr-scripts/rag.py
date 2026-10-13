import os
from dotenv import load_dotenv

# LangChain Components
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_groq import ChatGroq

from langchain.chains import RetrievalQA


# ---------------------------------------
# Load Environment Variables
# ---------------------------------------

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env")


# ---------------------------------------
# Step 1 : Load PDF
# ---------------------------------------

print("=" * 60)
print("Loading PDF...")
print("=" * 60)

loader = PyPDFLoader("C:/Users/kanna/Downloads/kannan_ac_ats_resume.pdf")

documents = loader.load()

print(f"Total Pages : {len(documents)}")


# ---------------------------------------
# Step 2 : Split into Chunks
# ---------------------------------------

print("\nSplitting Document...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks : {len(chunks)}")


# ---------------------------------------
# Step 3 : Create Embeddings
# ---------------------------------------

print("\nLoading Embedding Model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded")


# ---------------------------------------
# Step 4 : Store in Vector Database
# ---------------------------------------

print("\nCreating Chroma Vector Store...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Vector Database Created")


# ---------------------------------------
# Step 5 : Create Retriever
# ---------------------------------------

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

print("Retriever Ready")


# ---------------------------------------
# Step 6 : Load Groq LLM
# ---------------------------------------

print("\nLoading Groq LLM...")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

print("Groq Model Loaded")


# ---------------------------------------
# Step 7 : Retrieval QA Chain
# ---------------------------------------

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)


# ---------------------------------------
# Step 8 : Ask Questions
# ---------------------------------------

print("\n")
print("=" * 60)
print("PDF RAG Chatbot Started")
print("Type 'exit' to quit")
print("=" * 60)


while True:

    question = input("\nAsk Question : ")

    if question.lower() == "exit":
        break

    result = qa_chain.invoke(
        {"query": question}
    )

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(result["result"])

    print("\n" + "=" * 60)
    print("Retrieved Chunks")
    print("=" * 60)

    for i, doc in enumerate(result["source_documents"], start=1):

        print(f"\nChunk {i}")
        print("-" * 40)
        print(doc.page_content[:400])
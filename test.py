from modules.loader import load_documents
from modules.chunker import chunk_documents
from modules.embedder import build
from modules.retriever import retrieve

# Load and index documents before retrieving
raw_docs = load_documents("data")
chunks = chunk_documents(raw_docs)
build(chunks)

question="Who manages Apollo?"
docs = retrieve(question)
print(f"Retrieved {len(docs)} documents for question: {question}")
print(docs)
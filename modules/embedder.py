from sentence_transformers import SentenceTransformer
import faiss

model=SentenceTransformer(
        "all-MiniLM-L6-v2"
)

index=faiss.IndexFlatL2(384)

chunks=[]

def build(chunks_input):

    global chunks

    chunks=chunks_input

    vectors=model.encode(chunks)

    index.add(vectors)
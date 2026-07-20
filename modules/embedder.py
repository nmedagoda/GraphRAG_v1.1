from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model=SentenceTransformer(
        "all-MiniLM-L6-v2"
)

index=faiss.IndexFlatL2(384)

chunks=[]

def build(chunks_input):

        global chunks, index

        chunks.clear()
        chunks.extend(chunks_input)

        # Recreate the index each build so ids always align with current chunks.
        index=faiss.IndexFlatL2(384)

        if not chunks:
                return

        vectors=model.encode(chunks, convert_to_numpy=True)
        vectors=np.asarray(vectors, dtype="float32")

        index.add(vectors)
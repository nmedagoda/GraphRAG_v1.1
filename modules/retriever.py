import re
from modules import embedder

'''this retriver module is used to retrieve the relevant chunks from the vector database based on the question. 
It uses a combination of semantic search and keyword overlap to find the most relevant chunks.
But not using the graph to retrieve the answer. The graph is used to store the extracted entities and relationships from the chunks.'''


def _tokens(text):

    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))


def retrieve(question, top_k=3):

    chunks = embedder.chunks

    if not chunks:
        return []

    model = embedder.model
    index = embedder.index

    q=model.encode([question], convert_to_numpy=True)

    k=min(top_k, len(chunks), index.ntotal)

    semantic_hits=[]
    if k > 0:
        distance,ids=index.search(q, k)
        semantic_hits=[chunks[i] for i in ids[0] if 0 <= i < len(chunks)]

    # Keyword overlap fallback improves recall for explicit entity questions.
    question_tokens = _tokens(question)
    lexical_ranked = sorted(
        chunks,
        key=lambda c: len(question_tokens & _tokens(c)),
        reverse=True,
    )
    lexical_hits = [c for c in lexical_ranked if len(question_tokens & _tokens(c)) > 0]

    merged=[]
    for item in semantic_hits + lexical_hits:
        if item not in merged:
            merged.append(item)
        if len(merged) == top_k:
            break

    return merged
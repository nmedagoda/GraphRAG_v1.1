from modules.loader import load_documents
from modules.chunker import chunk_documents
from modules.entity_extractor import extract
from modules.graph_builder import add_to_graph
from modules.embedder import build
from modules.retriever import retrieve
from modules.generator import answer
from modules.hybrid_retriever import hybrid_retrieve

docs=load_documents("data")

chunks=chunk_documents(docs)

build(chunks)

for c in chunks:

    result=extract(c) # start to use LLM to extract entities and relationships from the chunk

    add_to_graph(result)

question="Who manages Apollo?"

context=retrieve(question)
# generate the answer using the retrieved context and the question without using the graph
print(answer(question,context))

# now uisng the graph to find the answer to the question
question2="What uses Apollo?"
context_graph = hybrid_retrieve(question2)

print(answer(question2, context_graph))

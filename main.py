from modules.loader import load_documents

from modules.chunker import chunk_documents

from modules.entity_extractor import extract

from modules.graph_builder import add_to_graph

from modules.embedder import build

from modules.retriever import retrieve

from modules.generator import answer

docs=load_documents("data")

chunks=chunk_documents(docs)

build(chunks)

for c in chunks:

    result=extract(c)

    add_to_graph(result)

question="Who manages Apollo?"

context=retrieve(question)

print(answer(question,context))
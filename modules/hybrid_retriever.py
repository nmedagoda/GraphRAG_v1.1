from modules.retriever import retrieve
from modules.graph_retriever import find_path
from modules.question_entities import extract_question_entities

def hybrid_retrieve(question):

    docs = retrieve(question)

    entities = extract_question_entities(question)

    graph_context = ""

    if len(entities) >= 2:

        path = find_path(
            entities[0],
            entities[1]
        )

        graph_context = str(path)

    context = f"""
Graph Context

{graph_context}

Document Context

{docs}
"""

    return context
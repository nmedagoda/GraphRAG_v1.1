from langchain_openai import ChatOpenAI
if __package__:
    from .retriever import retrieve
    from .prompt import SYSTEM_PROMPT
    from .config import MODEL_NAME
else:
    from retriever import retrieve
    from prompt import SYSTEM_PROMPT
    from config import MODEL_NAME


llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0
)


def ask(question):

    docs = retrieve(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
        {SYSTEM_PROMPT}

        Context

        {context}

        Question

        {question}
        """

    response = llm.invoke(prompt)

    return response.content
    #http://localhost:8000/docs
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma

from config import CHROMA_DB


embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory=CHROMA_DB,
    embedding_function=embeddings
)


def retrieve(question, k=4):

    docs = db.similarity_search(
        question,
        k=k
    )
    return docs
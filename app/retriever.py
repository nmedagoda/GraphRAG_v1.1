from langchain_openai import OpenAIEmbeddings

##from langchain_community.vectorstores import Chroma
##from langchain.vectorstores import Chroma
from langchain_chroma import Chroma

if __package__:
    from .config import CHROMA_DB
else:
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
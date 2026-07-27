'''This script reads every PDF, chunks the text and creates embeddings.'''
from langchain_community.document_loaders import PyPDFDirectoryLoader

##from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings

#from langchain_community.vectorstores import Chroma
##from langchain.vectorstores import Chroma
from langchain_chroma import Chroma

if __package__:
    from .config import PDF_FOLDER
    from .config import CHROMA_DB
else:
    from config import PDF_FOLDER
    from config import CHROMA_DB


def load_documents():

    loader = PyPDFDirectoryLoader(PDF_FOLDER)

    docs = loader.load()

    print(f"Loaded {len(docs)} pages")

    return docs


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks


def create_vector_db(chunks):

    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB
    )
    #db.persist()
    print("Vector database created")


def main():

    docs = load_documents()

    chunks = split_documents(docs)

    create_vector_db(chunks)


if __name__ == "__main__":
    main()
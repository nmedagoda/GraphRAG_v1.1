def chunk_documents(documents):

    chunks=[]

    for doc in documents:

        chunks.extend(doc.split("."))

    return [c.strip() for c in chunks if c.strip()]
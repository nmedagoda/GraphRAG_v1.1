from embedder import model,index,chunks

def retrieve(question):

    q=model.encode([question])

    distance,ids=index.search(q,3)

    return [chunks[i] for i in ids[0]]
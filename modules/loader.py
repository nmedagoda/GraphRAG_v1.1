from pathlib import Path

def load_documents(folder):

    docs=[]

    for file in Path(folder).glob("*.txt"):

        docs.append(file.read_text())

    return docs
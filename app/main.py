from fastapi import FastAPI

from pydantic import BaseModel

from rag import ask

app = FastAPI()


class Question(BaseModel):

    question: str


@app.get("/")
def root():

    return {"status": "running"}


@app.post("/ask")
def query(q: Question):

    answer = ask(q.question)

    return {
        "question": q.question,
        "answer": answer
    }
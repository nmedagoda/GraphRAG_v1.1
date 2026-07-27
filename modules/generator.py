from openai import OpenAI
import os
from dotenv import load_dotenv

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#client=OpenAI()
#client = OpenAI(api_key=)
client = OpenAI(api_key=OPENAI_API_KEY)
def answer(question,context):

    response=client.chat.completions.create(

        model="gpt-4.1",

        messages=[

        {
            "role":"system",

            "content":"Answer only from context."
        },

        {
            "role":"user",

            "content":

            f"""
Question:

{question}

Context

{context}
"""
        }]
    )

    return response.choices[0].message.content
from openai import OpenAI

client=OpenAI()

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
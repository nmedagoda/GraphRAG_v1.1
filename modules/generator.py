from openai import OpenAI

#client=OpenAI()
client = OpenAI(api_key="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")

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
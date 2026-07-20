from openai import OpenAI
import json

client=OpenAI()

PROMPT="""
Extract entities and relationships.

Return JSON.

Example

{
 "entities":["John","Apollo"],
 "relationships":[
   ["John","manages","Apollo"]
 ]
}

Text:
"""

def extract(chunk):

    response=client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {"role":"user",
             "content":PROMPT+chunk}
        ]
    )

    return json.loads(
        response.choices[0].message.content
    )
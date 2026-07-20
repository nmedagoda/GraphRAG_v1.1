from openai import OpenAI
import json
import re

#client=OpenAI()
client = OpenAI(api_key="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")

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
        response_format={"type": "json_object"},

        messages=[
            {"role":"user",
             "content":PROMPT+chunk}
        ]
    )

    content = response.choices[0].message.content or ""

    # Fallback: if the model includes markdown wrappers or extra prose,
    # extract the JSON object portion before parsing.
    if "```" in content:
        content = re.sub(r"^```(?:json)?", "", content.strip())
        content = re.sub(r"```$", "", content).strip()

    if not content:
        return {"entities": [], "relationships": []}

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", content)
        if not match:
            return {"entities": [], "relationships": []}
        data = json.loads(match.group(0))

    if not isinstance(data, dict):
        return {"entities": [], "relationships": []}

    entities = data.get("entities", [])
    relationships = data.get("relationships", [])

    if not isinstance(entities, list):
        entities = []
    if not isinstance(relationships, list):
        relationships = []

    return {
        "entities": entities,
        "relationships": relationships,
    }
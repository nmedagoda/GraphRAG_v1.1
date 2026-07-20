def extract_question_entities(question):

    entities=[]

    if "John" in question:
        entities.append("John")

    if "Python" in question:
        entities.append("Python")

    return entities
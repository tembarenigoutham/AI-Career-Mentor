skills_list = [
"python","machine learning","sql","java","html","css",
"javascript","tensorflow","nlp","deep learning",
"data analysis","pandas","numpy"
]

def extract_skills(text):

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
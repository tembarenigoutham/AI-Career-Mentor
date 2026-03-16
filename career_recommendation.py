import pandas as pd

def recommend_career(user_skills):

    data = pd.read_csv("skills_dataset.csv")

    best_role = ""
    best_score = 0

    for index,row in data.iterrows():

        role_skills = row["Skills"].split()

        score = len(set(user_skills) & set(role_skills))

        if score > best_score:
            best_score = score
            best_role = row["Role"]

    return best_role
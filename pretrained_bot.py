import json
import os

with open("data/daily_questions.json", "r") as file:
    responses = json.load(file)

def get_response(question):
    for key in responses:
        if key in question:
            return responses[key]
    return "Bunu anlayamadim."

while True:
    question = input("Sen: ")
    answer = get_response(question.lower())
    print("Vector:", answer)
    os.system(f'espeak-ng -v tr "{answer}"')

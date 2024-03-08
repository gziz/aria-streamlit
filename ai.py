
import os
import requests

API_URL = os.getenv("ARIA_API_URL")
def send_question(text: str):
    payload = {"message": {"text": text}}
    QUESTION_URL = API_URL + "/question"
    response = requests.post(QUESTION_URL, json=payload)
    res_json = response.json()
    return res_json["answer"]
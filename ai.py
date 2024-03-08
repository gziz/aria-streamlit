
import os
import requests

URL = os.getenv("ARIA_API_URL")
def send_question(text: str):
    payload = {"message": {"text": text}}
    print(payload)
    response = requests.post(URL, json=payload)
    res_json = response.json()
    return res_json["answer"]
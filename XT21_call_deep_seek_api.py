
import requests


def get_url():
    return r"http://10.1.24.2:19980/deepseek/"


def chat_api(prompt):
    resp = requests.post(
        url=get_url(),
        json={"prompt": prompt},
        headers={"Content-Type": "application/json;charset=utf-8"}
    )
    return resp.json()['response']

if __name__ == '__main__':

    question = "hi"
    response = chat_api(question)
    print('Answer:', response)

import requests


def get_url():
    return "http://127.0.0.1:8008"

def chat_with_api(prompt):
    resp = requests.post(
        url=get_url(),
        json={"prompt": prompt},
        headers={"Content-Type": "application/json;charset=utf-8"}
    )
    return resp.json()['response']

if __name__ == '__main__':
    question = "在蛇年，我应该怎么学习Python? "
    response = chat_with_api(question)
    print('Answer:', response)

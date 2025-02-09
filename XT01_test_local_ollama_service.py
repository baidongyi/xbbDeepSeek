import requests


def chat_with_local_deep_seek(text:str):

    url = 'http://localhost:11434/api/generate'

    post_json = {
            "model": "deepseek-r1:8b",
            "prompt": f"{text}",
            "stream": False
        }

    response = requests.post(url,json=post_json)
    text = response.json()["response"]
    return text

if __name__ == "__main__":
    ask = "我怎么才能提高初中数学成绩"
    res = chat_with_local_deep_seek(ask)

    print(res)
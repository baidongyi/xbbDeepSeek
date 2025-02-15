import os.path

from fastapi import FastAPI, Request
import uvicorn, json, datetime

from XT01_test_local_ollama_service import chat_with_local_deep_seek

import sys
import os

from fastapi.middleware.cors import CORSMiddleware


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

app = FastAPI()

# 允许所有域名访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers={"*"},
)


@app.post("/")
async def create_item(request: Request):

    json_post_raw = await request.json()
    json_post = json.dumps(json_post_raw)
    json_post_list = json.loads(json_post)
    prompt = json_post_list.get('prompt')

    res=chat_with_local_deep_seek(prompt)

    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    answer = {
        "response": res,
        "status": 200,
        "time": time
    }
    log = "[" + time + "] " + '", prompt:"' + prompt + '", response:"' + repr(res) + '"'
    print(log)
    return answer


if __name__ == '__main__':

    uvicorn.run(app, host='0.0.0.0', port=8008, workers=1)

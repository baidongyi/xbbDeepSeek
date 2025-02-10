import ollama


def chat_with_ollama(prompt:str):
    response = ollama.chat(model='deepseek-r1:8b',  # 选择模型
                           messages=[{'role': 'user', 'content': prompt}])
    result = response['message']['content']
    return result

if __name__ == "__main__":
    prompt = "你是谁"
    res=chat_with_ollama(prompt)
    print(res)

import gradio as gr


from XT21_call_deep_seek_api import chat_api


def modify_res(text:str):
    t=text.replace("<think>","# **我的思考过程如下：**\n")
    t=t.replace("</think>","# **思考结束，以下是我的回答:**\n")
    return t


def chat(text, history):
    res = chat_api(text)
    res= modify_res(res)
    print(f"ask={text}, \nres={res}")
    return res



if __name__ == "__main__":
    app = gr.ChatInterface(chat,title="智能助手小白白[Deep Seek R1]")
    app.launch(inbrowser=True)

import os
from openai import OpenAI
from keys import API_DS


def respons_ds(text: str) -> str:
    dialog = []
    dialog = dialog[-20:]
    messages = [{"role": "system", "content": "Ты ассистент ребенка. Твой ответ всегда состоит из 3 слов!"}]

    client = OpenAI(api_key=API_DS, base_url="https://api.deepseek.com")
    dialog.append({"role": "user", "content": text})
    for i in dialog:
        messages.append(i)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False)
    


    full_response = response.choices[0].message.content
    dialog.append({"role": "assistant", "content": full_response})
    #print(full_response)
    return full_response


# for chunk in response:
#     content = chunk.choices[0].delta.content
#     if content:
#         print(content, end="", flush=True)


# .\.venv\Scripts\Activate
# pip3 install openai
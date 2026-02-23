import os
from openai import OpenAI
from keys import API_DS


dialog = []

dialog = [
    {"role": "user", "content": "Привет как дела?"},
    {"role": "assistant", "content": " В целом норм.."},
    {"role": "user", "content": "Ясно.."}
]
dialog = dialog[3:]

def respons_ds(text: str) -> str:
    client = OpenAI(api_key=API_DS, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Ты ассистент ребенка. Твой ответ всегда состоит из 3 слов!"},
            {"role": "user", "content": text},
            # {"role": "assistant", "content": answer}
        ],
        stream=False)


    full_response = response.choices[0].message.content
    #print(full_response)
    return full_response


# for chunk in response:
#     content = chunk.choices[0].delta.content
#     if content:
#         print(content, end="", flush=True)


# .\.venv\Scripts\Activate
# pip3 install openai
import os
from openai import OpenAI
from keys import API_DS


client = OpenAI(api_key=API_DS, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "ты учитель биологии у 5 класса, отвечаешь экстримально коротко"},
        {"role": "user", "content": "как живут медведи?"},
    ],
    stream=True
)

for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)


# .\.venv\Scripts\Activate
# pip3 install openai
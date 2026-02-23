# pip install --upgrade requests
# pip install requests[socks]
import requests
import base64
from keys import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXY_HTTP, PROXY_SOCKS5H




def transcription(name_file: str) -> str:

    url = f"http://{HOST}/api/openai-voice-to-text/"

    headers = {
        API_KEY: VALUE_KEY,
        "User-Agent": "Mozilla/5.0"
    }

    with open(f'./{name_file}', 'rb') as f:
        
        files = {
            'file': (name_file, f),
            'access_id': (None, ACCESS_ID),
            'prompt': (None, "переведи в текст"),
            'model': (None, "whisper-1"),
            'response_format': (None, "text")
        }

        response = requests.post(url, headers=headers, proxies=PROXY_SOCKS5H, files=files, timeout=200)

    if response.status_code == 200:
        answer_api = response.json()
        text_answer = answer_api.get("response")
        return text_answer
    else:
        print(response.status_code, response.text)




def get_voice(text):

    url = f"http://{HOST}/api/openai-text-to-voice/"

    data = {
        "access_id": ACCESS_ID,
        "user_content": text,
        "voice": "nova", # alloy, echo, fable, onyx, nova, and shimmer
        "model": "tts-1", # tts-1 or tts-1-hd
        "response_format": "wav", # mp3, opus, aac, flac, wav, and pcm
        "speed": 1.0, # 0.25 to 4.0
    }

    headers = {
        API_KEY: VALUE_KEY,
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, headers=headers, data=data, proxies=PROXY_SOCKS5H, timeout=200)

    format_audio = data["response_format"]

    if response.status_code == 200:
        # Получаем JSON-ответ
        json_response = response.json()
        b64_json = json_response.get("b64_json")

        if b64_json:
            # Декодируем строку Base64 обратно в бинарные данные
            audio_data = base64.b64decode(b64_json)

            # Сохраняем аудиофайл локально
            name_file = f"output_audio.{format_audio}"
            with open(f"./{name_file}", "wb") as audio_file:
                audio_file.write(audio_data)

            print(f"The audio file is saved as {name_file}")
            return name_file

        elif isinstance(response, str):
            print(f"Error: {response}")

    else:
        if isinstance(response, str):
            print(f"Error: {response}")
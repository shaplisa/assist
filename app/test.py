# import subprocess
# import os

# def play_audio(filename):
#     """
#     Воспроизведение аудиофайла через aplay с авто-конвертацией
#     """
    
#     if not os.path.exists(filename):
#         print(f"Ошибка: файл {filename} не найден")
#         return False
    
#     # Конвертируем через sox "на лету"
#     cmd = f"sox {filename} -b 32 -c 2 -t wav - | aplay"
    
#     try:
#         print(f"Воспроизведение {filename}...")
#         result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
#         print("Воспроизведение завершено")
#         return True
        
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка воспроизведения: {e}")
#         print(f"stderr: {e.stderr}")
#         return False

# # Использование:
# # play_audio("output_audio.wav")


# # 1. 
# dialog = [
#     {"role": "user", "content": "Привет как дела?"},
#     {"role": "assistant", "content": " В целом норм.."},
#     {"role": "user", "content": "Ясно.."}
# ]
# dialog = dialog[-2:]
# print(dialog)

# # 2.


elif status_hold == False and recording_active:
    print("Останавливаю запись...")
    speechkit.change_recording_active(False)
    
    if record_thread:
        record_thread.join()
        # После join поток гарантированно завершён
        # и last_transcription уже сохранён
    
    record_thread = None
    
    # Читаем результат
    input_question = speechkit.get_last_transcription()
    print("input_question:", input_question)
    
    # Дальше идёт обработка - это нормально, не надо continue
    if input_question and input_question.strip():
        text_stream_ds = deepseek.stream_llm_response(input_question)
        speechkit.stream_synthesis(text_stream_ds)
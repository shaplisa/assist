import subprocess
import numpy as np
import wave
import os

# ===== НАСТРОЙКИ =====
filename = "запись.wav"
seconds = 10
gain = 3.0  # во сколько раз усилить (можно 2, 3, 4...)

print(f"🎤 Запись {seconds} секунд...")

# 1. Записываем через arecord (тихо, но работает)
subprocess.run([
    "arecord",
    "-D", "hw:0,0",
    "-f", "S32_LE",
    "-r", "48000",
    "-c", "2",
    "-d", str(seconds),
    "temp.wav"
])

print("🔊 Усиливаем...")

# 2. Читаем WAV файл
with wave.open("temp.wav", 'rb') as wf:
    frames = wf.getnframes()
    rate = wf.getframerate()
    channels = wf.getnchannels()
    sampwidth = wf.getsampwidth()
    data = wf.readframes(frames)

# 3. Превращаем байты в числа (32 бита)
samples = np.frombuffer(data, dtype=np.int32)

# 4. Усиливаем
samples = samples * gain

# 5. Защита от искажений (чтобы не вылезти за пределы)
max_val = 2**31 - 1
min_val = -2**31
samples = np.clip(samples, min_val, max_val)

# 6. Превращаем обратно в байты
data_boosted = samples.astype(np.int32).tobytes()

# 7. Сохраняем усиленный файл
with wave.open(filename, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(rate)
    wf.writeframes(data_boosted)

# 8. Удаляем временный файл
os.remove("temp.wav")

# 9. Результат
size = os.path.getsize(filename) / 1024
print(f"✅ Готово! Файл: {filename}")
print(f"📊 Размер: {size:.1f} КБ")
print(f"🔊 Усиление в {gain} раза")
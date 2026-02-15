import subprocess
import time
import os


def get_audio_mic() -> str:
    """Получаем аудио с микрофона"""

    # ===== НАСТРОЙКИ =====
    filename = "moy_golos.wav"  # имя файла
    seconds = 10                 # сколько секунд записывать

    print(f"🎤 Запись {seconds} секунд...")
    print("Говори что хочешь")
    print("-" * 30)

    # Запись в 48 кГц, стерео
    process = subprocess.Popen([
        "arecord",
        "-D", "hw:0,0",
        "-f", "S32_LE",
        "-r", "48000",
        "-c", "2",
        "-d", str(seconds),
        "temp_48k_stereo.wav"
    ])
    process.wait()

    # Конвертируем в 16 кГц, моно (через sox)
    print("🔄 Конвертируем в 16 кГц, моно...")
    os.system(f"sox temp_48k_stereo.wav -r 16000 -c 1 {filename}")

    # Удаляем временный файл
    os.remove("temp_48k_stereo.wav")

    print("\n✅ Готово!")

    if os.path.exists(filename):
        size = os.path.getsize(filename) / 1024
        print(f"📁 Файл: {filename}")
        print(f"📊 Размер: {size:.1f} КБ")
        return filename
import subprocess
# import threading
import time
import os




class Audio:
    def __init__(self):
        self.record_process = None
        self.recording_active = False

    
    def get_recording_active(self):
        return self.recording_active
    
    def change_recording_active(self, status: bool):
        self.recording_active = status


    def record_audio(self, filename="test.wav") -> str:
        """Запись аудио через arecord"""
        cmd = [
            "arecord", 
            "-f", "S16_LE",      # 16 бит вместо 32
            "-c", "1",            # моно вместо стерео
            "-r", "16000",        # 16 кГц вместо 44.1 кГц
            filename
        ]
        # Запускаocем процесс
        subprocess.Popen(
            cmd, 
            stdout=subprocess.DEVNULL,  # подавляем вывод
            stderr=subprocess.DEVNULL   # подавляем ошибки
        )
        # Ждем пока recording_active == True
        while self.recording_active:
            time.sleep(0.1)
        
        # Останавливаем запись
        if self.record_process:
            self.record_process.terminate()
            try:
                self.record_process.wait(timeout=1)
            except subprocess.imeToutExpired:
                self.record_process.kill()  # если не завершился, убиваем принудительно
        
        print(f"Запись сохранена в {filename}")
        return filename


    @staticmethod
    def play_audio(filename: str, gain_db=10) -> bool:
        """
            Воспроизведение аудиофайла с усилением через play (sox)
            
            Параметры:
            filename - путь к аудиофайлу для воспроизведения
            gain_db - усиление в дБ (по умолчанию 20)
        """
        # Проверяем, существует ли файл
        if not os.path.exists(filename):
            print(f"Ошибка: файл {filename} не найден")
            return False
        
        # Команда play с усилением
        cmd = ["play", filename, "gain", str(gain_db)]
        
        try:
            print(f"Воспроизведение {filename} с усилением {gain_db} дБ...")
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("Воспроизведение завершено")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Ошибка воспроизведения: {e}")
            print(f"stderr: {e.stderr}")
            return False
        
        except FileNotFoundError:
            print("Ошибка: play не найден. Установите sox: sudo apt install sox")
            return False



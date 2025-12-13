import subprocess
import sys

def connect_to_wifi(ssid: str, password: str) -> bool:
    command = [
        "sudo", "nmcli", "device", "wifi", "connect", ssid, 
        "password", password
    ]

    try:
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            check=True
        )
        print(f"Успешно подключено к {ssid}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Ошибка подключения к {ssid}.")
        print(f"Детали: {e.stderr.strip()}")
        return False
    except FileNotFoundError:
        print("Ошибка: Утилита nmcli не найдена. Убедитесь, что используется NetworkManager.")
        return False
    
connect_to_wifi("Milano","ash")
import subprocess
import sys
from config import WIFI, SUDO_PASS
import time


def ip() -> str:
    try:
        result = subprocess.check_output(["hostname", "-I"]).decode().strip()
        ip = result.split()
        return ip[0] if ip else None
        
    except Exception as e:
        print(f"Error get_ip_address: {e}")
        return False
    

def connect_to_wifi(ssid: str, password: str) -> bool:
    command = [
        "sudo", "-S", "nmcli", "device", "wifi", "connect", ssid, 
        "password", password
    ]

    try:

        proc = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        output, error = proc.communicate(input = SUDO_PASS + "\n", timeout=30)
        result = output + error


        if "successfully" in result.lower():
            print(f"rr Successfully connected to {ssid}")
            time.sleep(1)
            ip1 = ip()
            if ip1:
                return True
        else:
            print(f"rr Connection failed: {result}")
            return False



        # if "successfully" in result.lower():
        #     print(f"Successfully connected to {ssid}")
        #     return True
        # else:
        #     print(f"Connection failed: {result}")
        #     return False
    
        
    except subprocess.CalledProcessError as e:
        print(f"Ошибка подключения к {ssid}.")
        print(f"Детали: {e.stderr.strip()}")
        return False
    
    except FileNotFoundError:
        print("Ошибка: Утилита nmcli не найдена. Убедитесь, что используется NetworkManager.")
        return False


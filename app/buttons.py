#!/usr/bin/env python3
import RPi.GPIO as GPIO
from config import BUTTON_OFF_PIN, BUTTON_PIN

def status_button(name_button) -> bool | None:
    """ Абстрактная функция получения статуса кнопки"""
    try:  
        if GPIO.input(name_button) == GPIO.LOW:
            return True
        else:
            return False

    except KeyboardInterrupt:
        return None

# try:
#     while True:
#         # if GPIO.input(BUTTON_PIN) == GPIO.LOW:
#         #     print("Сработала кнопка ")
#         #     time.sleep(0.2)  # защита от дребезга
        
#         if GPIO.input(BUTTON_OFF_PIN) == GPIO.LOW:
#             print("Устройство выключается")

#             time.sleep(0.2)
        
#         time.sleep(0.01)

# except KeyboardInterrupt:
#     GPIO.cleanup()

#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time



# Настройка пинов (BCM нумерация)
# BUTTON_PIN = 5   # GPIO5 (физический пин 29)
# BUTTON_OFF_PIN = 6   # GPIO6 (физический пин 31)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(BUTTON_OFF_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# print("Ожидание нажатия кнопок (Ctrl+C для выхода)...")


def status_button(name_button):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(name_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
            
        if GPIO.input(name_button) == GPIO.LOW:
            print("кнопка выключения сработала")
            time.sleep(0.2)
            return True

    except KeyboardInterrupt:
        GPIO.cleanup()
        return False







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

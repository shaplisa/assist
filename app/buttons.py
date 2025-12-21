#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Настройка пинов (BCM нумерация)
BUTTON1_PIN = 5   # GPIO5 (физический пин 29)
BUTTON2_PIN = 6   # GPIO6 (физический пин 31)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Ожидание нажатия кнопок (Ctrl+C для выхода)...")

try:
    while True:
        if GPIO.input(BUTTON1_PIN) == GPIO.LOW:
            print("Сработала кнопка 1")
            time.sleep(0.2)  # защита от дребезга
        
        if GPIO.input(BUTTON2_PIN) == GPIO.LOW:
            print("Сработала кнопка 2")
            time.sleep(0.2)
        
        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()

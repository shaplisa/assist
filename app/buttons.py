#!/usr/bin/env python3
"""Пришлось временно использовать для двух разных плат, позже изменить.."""
import time
import RPi.GPIO as GPIO
from config import BUTTON_OFF_PIN, BUTTON_PIN, GPIO_AMP, MOTHERBOARD



class Gpio:
    def __init__(self):
        if MOTHERBOARD == "ORANGE":
            self.button_ip = BUTTON_OFF_PIN
            self.button_speek = BUTTON_PIN
            self.out_amp = GPIO_AMP
            self._init_buttons()
            self._init_outs()
        elif MOTHERBOARD == "RASPBERRY":
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(BUTTON_OFF_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    # RASPBERRY:
    @staticmethod
    def status_button(name_button) -> bool | None:
        """ Абстрактная функция получения статуса кнопки для RASPBERRY"""
        try:  
            if GPIO.input(name_button) == GPIO.LOW:
                return True
            else:
                return False

        except KeyboardInterrupt:
            GPIO.cleanup()
            return None


    # ORANGE:
    def _init_buttons(self):
        # Настройка GPIO кнопок
        for gpio_one in [self.button_ip, self.button_speek]:
            try:
                with open('/sys/class/gpio/export', 'w') as f:
                    f.write(str(gpio_one))
                time.sleep(0.1)
                with open(f'/sys/class/gpio/gpio{gpio_one}/direction', 'w') as f:
                    f.write('in')
                #print(f"GPIO {gpio_one} настроен")
            except Exception as e:
                print(f"GPIO {gpio_one} уже настроен: {e}")


    def _init_outs(self):
        # Настройка GPIO для усилителя
        try:
            with open('/sys/class/gpio/export', 'w') as f:
                f.write(str(self.out_amp))
            time.sleep(0.1)
            with open(f'/sys/class/gpio/gpio{self.out_amp}/direction', 'w') as f:
                f.write('out')
            #print(f"GPIO {self.out_amp} настроен как выход для усилителя")

            # Устанавливаю низкий уровень (0V)
            with open(f'/sys/class/gpio/gpio{self.out_amp}/value', 'w') as f:
                f.write('0')

        except Exception as e:
            print(f"GPIO {self.out_amp} уже настроен: {e}")

        # Принудительно выключаю AMP
        with open(f'/sys/class/gpio/gpio{self.out_amp}/value', 'w') as f:
            f.write('0')
            #print("Установлен как 0")

        ####


    def button_ip_status(self):
        with open(f'/sys/class/gpio/gpio{self.button_ip}/value', 'r') as f:
            btnip = int(f.read().strip())
        return btnip


    def button_speek_status(self):
        with open(f'/sys/class/gpio/gpio{self.button_speek}/value', 'r') as f:
            btn2 = int(f.read().strip())
        return btn2


    def off_amp(self):
        with open(f'/sys/class/gpio/gpio{self.out_amp}/value', 'w') as f:
            f.write('0')
        #print("Выключил усилок")


    def on_amp(self):
        with open(f'/sys/class/gpio/gpio{self.out_amp}/value', 'w') as f:
            f.write('1')
        #print("Включил усилок")
        time.sleep(0.05)











# import RPi.GPIO as GPIO
# from config import BUTTON_OFF_PIN, BUTTON_PIN






# GPIO.setmode(GPIO.BCM)
# GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(BUTTON_OFF_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)



# def status_button(name_button) -> bool | None:
#     """ Абстрактная функция получения статуса кнопки"""
#     try:  
#         if GPIO.input(name_button) == GPIO.LOW:
#             return True
#         else:
#             return False

#     except KeyboardInterrupt:
#         GPIO.cleanup()
#         return None










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

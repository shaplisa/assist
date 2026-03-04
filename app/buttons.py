#!/usr/bin/env python3
import time
from config import BUTTON_OFF_IP, BUTTON_SPEEK, GPIO_AMP, MOTHERBOARD



class Gpio:
    def __init__(self):
        """В зависимости от платы orange/rasp, инициализируются кнопки из config.py"""
        self.motherboard = MOTHERBOARD
        self.button_ip = BUTTON_OFF_IP
        self.button_speek = BUTTON_SPEEK
        self.out_amp = GPIO_AMP
        self._init_outs()
        self._init_buttons()


    def _init_buttons(self):
        """Инициализация и настройка кнопок"""
        if self.motherboard == "RASPBERRY":
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.button_speek, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.button_ip, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        elif self.motherboard == "ORANGE":
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


    def status_button(self, name_button) -> bool | None:
        """Получение статуса кнопки RASPBERRY/ORANGE"""
        if self.motherboard == "RASPBERRY":
            try:  
                if GPIO.input(name_button) == GPIO.LOW: return True
                else: return False
            except KeyboardInterrupt:
                GPIO.cleanup()
                return None
            
        elif self.motherboard == "ORANGE":
            try:
                with open(f'/sys/class/gpio/gpio{name_button}/value', 'r') as f:
                    btnip = int(f.read().strip())
                    if btnip == 1: return False
                    elif btnip == 0: return True
            except KeyboardInterrupt:
                return None


    def _init_outs(self):
        """Настройка GPIO Stand By для усилителя"""
        if self.motherboard == "ORANGE":
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

        elif self.motherboard == "RASPBERRY":
            pass


    def off_amp(self):
        """Выключить усилитель"""
        if self.motherboard == "ORANGE":
            with open(f'/sys/class/gpio/gpio{self.out_amp}/value', 'w') as f:
                f.write('0')
            #print("Выключил усилок")

        elif self.motherboard == "RASPBERRY":
            pass


    def on_amp(self):
        """Включить усилитель"""
        if self.motherboard == "ORANGE":
            with open(f'/sys/class/gpio/gpio{self.out_amp}/value', 'w') as f:
                f.write('1')
            #print("Включил усилок")
            time.sleep(0.05)

        elif self.motherboard == "RASPBERRY":
            pass

from config import WIFI, SUDO_PASS, BUTTON_OFF_PIN, BUTTON_PIN
# from luma.core.interface.serial import i2c
# from luma.oled.device import ssd1306
# from PIL import Image, ImageDraw, ImageFont
from network import connect_to_wifi, ip
import time
from buttons import status_button
import subprocess
from display import image 
flag_hold = 0







# serial = i2c(port=1, address=0x3C)
# device = ssd1306(serial, width=128, height=64)


# def image(text, x, y):
#     image = Image.new('1', (device.width, device.height))
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.load_default()
#     draw.text((x, y), text, font=font, fill=255)
#     device.display(image)


def main() -> None:
    while True:

        get_ip = ip()

        if not get_ip:
            print("wifi is not")
            image("wifi is not", 5, 10)
            

            # for a in WIFI:
            #     r = connect_to_wifi(a.get("ssid"), a.get("password"))
            #     if r == True:
            #         return
            #     time.sleep(5)
        else:
            print(f"ip is: {get_ip}")
            image(get_ip, 5, 10)


        
        status_but = status_button(BUTTON_OFF_PIN) 
        if status_but == True:

            print("выключаюсь")
            image("i am powering off(",5,20)
            time.sleep(1)
            
            command = ["sudo", "poweroff"]

            proc = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            proc.communicate(input = SUDO_PASS + "\n", timeout=30)

            

        status_hold = status_button(BUTTON_PIN)
        if status_hold == True and flag_hold > 10:
            
            image("идёт запись звука", 5, 20)
            
        elif status_hold == True:
            flag_hold += 1
        else:
            flag_hold = 0
        

        




        time.sleep(0.2)

main()




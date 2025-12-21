from config import WIFI
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
from network import connect_to_wifi, ip
import time



serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)


def image(text, x, y):
    image = Image.new('1', (device.width, device.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((x, y), text, font=font, fill=255)
    device.display(image)





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


        time.sleep(2)

main()
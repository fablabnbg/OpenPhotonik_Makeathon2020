#

from machine_esp32_heltec_LoRa32 import *
from rgb_led import *


def setup_rgb():
    pass

def rgb_led_update_co2(r_co2):
    if r_co2 < 1000:
        rgb_led_update("green")
    elif (r_co2 >= 1000) and (r_co2 < 1500):
        rgb_led_update("yellow")
    elif (r_co2 >= 1500) and (r_co2 < 1800):
        rgb_led_update("red")
    elif (r_co2 >= 1800) and (r_co2 < 2000):
        rgb_led_update("red")
        blink(2)
    elif r_co2 >= 2000:
        rgb_led_update("red")
        blink(4)
    else:
        led_off()


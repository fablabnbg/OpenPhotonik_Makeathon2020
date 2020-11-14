# 

import time
#
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
from machine_esp32_heltec_LoRa32 import *

reset_pin_oled = Pin(pin_OLED_RST,Pin.OUT, value=0)
scl_pin_oled   = Pin(pin_OLED_SCL, Pin.IN, Pin.PULL_UP)
sda_pin_oled   = Pin(pin_OLED_SDA, Pin.IN, Pin.PULL_UP)

DEBUG = True

oled  = None

def setup_oled():
    global oled
    # create reset pulse
    reset_pin_oled.off();
    time.sleep_ms(200)
    reset_pin_oled.on();

    i2c_oled = I2C(scl=scl_pin_oled, sda=sda_pin_oled,  freq=400000)

    oled = SSD1306_I2C(128,64,i2c_oled)
    if DEBUG:
        idev_oled = i2c_oled.scan()
        print("idev=");
        print(idev_oled)
    return oled

# Diese Funktion dient unserer Bequemlichkeit
def text_line(text, line, pos = 0):
    x = 10 * pos;
    y = line * 11
    oled.text(text,x,y)

def oled_update_co2(r_co2):
    oled.fill(0)
    text_line("Der CO2-wert",  0,0)
    text_line("in diesem Raum",1,0)
    text_line("betraegt",      2,2)
    text_line(str(r_co2),      4,2)
    text_line("ppm",           4,2+len(str(r_co2)) )
    oled.rect(0,38,128,20,1)
    oled.show()


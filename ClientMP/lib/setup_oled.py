# 
import time
import ubinascii
import machine
#
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
from machine_esp32_heltec_LoRa32 import *

reset_pin_oled = Pin(pin_OLED_RST,Pin.OUT, value=0)
scl_pin_oled   = Pin(pin_OLED_SCL, Pin.IN, Pin.PULL_UP)
sda_pin_oled   = Pin(pin_OLED_SDA, Pin.IN, Pin.PULL_UP)

DEBUG = True

oled  = None
SENS_ID = ubinascii.hexlify(machine.unique_id()[3:])

def setup_oled():
    global oled
    # create reset pulse
    reset_pin_oled.off();
    time.sleep_ms(200)
    reset_pin_oled.on();

    i2c_oled = I2C(scl=scl_pin_oled, sda=sda_pin_oled,  freq=400000)

    oled = SSD1306_I2C(128, 64, i2c_oled)
    if DEBUG:
        idev_oled = i2c_oled.scan()
        print("idev_oled= ", end='');
        print(idev_oled)
    return oled

# Diese Funktion dient unserer Bequemlichkeit
def text_line(text, line, pos = 0):
    x = 10 * pos;
    y = line * 11
    oled.text(text,x,y)

def oled_update_co2(r_co2, r_temp, r_hum):
    s_id = SENS_ID.decode("utf-8")
    oled.fill(0)
    text_line("S_ID: %s"     % str(s_id),   0,0)
    text_line("temp: %s C"   % str(r_temp), 1,0)
    text_line("hum : %s %%  RH" % str(r_hum),  2,0)
    text_line("co2 : %sppm"  % str(r_co2),  4,0)
    oled.rect(0,38,128,20,1)
    oled.show()

### main
if __name__ == '__main__':
    setup_oled()
    oled_update_co2(   -1, 10.0, 30)
    time.sleep_ms(2000)
    oled_update_co2(  500, 10.1, 31)
    time.sleep_ms(2000)
    oled_update_co2( 1000, 10.2, 32)
    time.sleep_ms(2000)
    oled_update_co2( 1500, 10.3, 33)
    time.sleep_ms(2000)
    oled_update_co2( 2000, 10.4, 34)
    time.sleep_ms(2000)
    oled_update_co2( 3000, 10.5, 35)
    time.sleep_ms(2000)
    oled_update_co2( 3000, 10.5, 35)
    time.sleep_ms(2000)
    oled_update_co2(33310, 10.6, 36)
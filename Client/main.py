print('\n### OpenPhotonik_Makeathon2020\n')

import time, utime
from machine_esp32_heltec_LoRa32 import *
from machine import Pin, I2C
from time import sleep
from rgb_led import *
from ssd1306 import SSD1306_I2C

from scd30 import SCD30
from setup_co2 import *
from scd30 import SCD30

scd30 = co2_attach()


reset_pin_oled = Pin(pin_OLED_RST,Pin.OUT, value=1)
scl_pin_oled   = Pin(pin_OLED_SCL, Pin.IN, Pin.PULL_UP)
sda_pin_oled   = Pin(pin_OLED_SDA, Pin.IN, Pin.PULL_UP)

led_off()

i2c_oled = I2C(scl=scl_pin_oled, sda=sda_pin_oled,  freq=400000)

idev_oled = i2c_oled.scan()
print("idev=");
print(idev_oled)

oled = SSD1306_I2C(128,64,i2c_oled)

# Diese Funktion dient unserer Bequemlichkeit
def text_line(text, line, pos = 0):
    x = 10 * pos;
    y = line * 11
    oled.text(text,x,y)

###

cnt = 0
err = 0
start_time = utime.ticks_ms()
while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    diff = utime.ticks_ms() - start_time
    try:
        while scd30.get_status_ready() != 1:
            time.sleep_ms(200)
        cnt += 1
        result = scd30.read_measurement()
    except OSError:
        err += 1
        result = 'skipped'
    if err:
        quot = cnt/err
    else:
        quot = cnt
    print("%6d.%03d: " % (diff/1000,diff%1000), end = '')
    print("%3d/%3d/%3d, " % (cnt,err, quot), end = '')
    print( result )

    if result == "skipped":
        continue     # start while loop over again

    ### here we have a real value so we can updte the display and LED
    r_co2, r_temp, r_hum = result    # assign tupel to named variables
    r_co2 = int(r_co2)
    oled.fill(0)
    text_line("Der CO2-wert",  0,0)
    text_line("in diesem Raum",1,0)
    text_line("betraegt",      2,2)
    text_line(str(r_co2),      4,2)
    text_line("ppm",           4,2+len(str(r_co2)) )
    oled.rect(0,38,128,20,1)
    oled.show()

    if r_co2 < 1000:
        led_color("green")
    elif (r_co2 >= 1000) and (r_co2 < 1500):
        led_color("yellow")
    elif (r_co2 >= 1500) and (r_co2 < 1800):
        led_color("red")
    elif (r_co2 >= 1800) and (r_co2 < 2000):
        led_color("red")
        blink(2)
    elif r_co2 >= 2000:
        led_color("red")
        blink(4)
    else:
        led_off()

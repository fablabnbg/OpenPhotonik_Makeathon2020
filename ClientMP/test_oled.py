#
# import upip
# upip.install('micropython-ssd1306')
from machine_esp32_heltec_LoRa32 import *
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Heltec LoRa32-board mit  OLED Display

reset_pin = Pin(pin_OLED_RST,Pin.OUT, value=1)
scl_pin   = Pin(pin_OLED_SCL, Pin.IN, Pin.PULL_UP)
sda_pin   = Pin(pin_OLED_SDA, Pin.IN, Pin.PULL_UP)

i2c = I2C(scl=scl_pin, sda=sda_pin,  freq=400000)

idev = i2c.scan()
print("idev=");
print(idev)

# Einfache Demo mit OLED - Display

# Wir benötigen eine I2C - Schnittstelle

# Aktivieren des Moduls

# Das OLED wird initialisiert
oled = SSD1306_I2C(128,64,i2c)

# Diese Funktion dient unserer Bequemlichkeit
def text_line(text, line, pos = 0):
    x = 10 * pos;
    y = (line) * 11
    oled.text(text,x,y)
    
# Das Hauptprogramm    
oled.fill(0)
text_line("Hallo! Ich bin",0,1)
text_line("ein ESP32,",1,3)
text_line("programmiert in",2,0)
text_line("Micropython",4,2)
oled.rect(0,38,128,20,1)
oled.show()
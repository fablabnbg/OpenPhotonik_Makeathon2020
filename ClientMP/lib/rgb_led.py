#
from machine import Pin
from time import sleep
from machine_esp32_heltec_LoRa32 import *

redPin   = Pin(pin_RGB_r, Pin.OUT)
greenPin = Pin(pin_RGB_g, Pin.OUT)
bluePin  = Pin(pin_RGB_b, Pin.OUT)

def rgb_led_update(color):
    if color == "off":
        greenPin.value(0)
        bluePin.value(0)
        redPin.value(0)
    elif color == "green":
        greenPin.value(1)
        bluePin.value(0)
        redPin.value(0)
    elif color == "yellow":
        greenPin.value(1)
        bluePin.value(0)
        redPin.value(1)
    elif color == "red":
        greenPin.value(0)
        bluePin.value(0)
        redPin.value(1)
    else:
        greenPin.value(0)
        bluePin.value(0)
        redPin.value(0)
 

def blink(freq):
    greenPin.value(0)
    bluePin.value(0)
    if str(freq).isdigit:
        for i in range(freq):
            redPin.value(1)
            sleep(1/freq*2)
            redPin.value(0)
            sleep(1/freq*2)
            i = i+1
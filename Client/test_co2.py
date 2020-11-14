# Heltec LoRa32-board mit  OLED Display

import time, utime

from machine_esp32_heltec_LoRa32 import *
from machine import Pin, I2C
from scd30 import SCD30


### configure i2c-pins
scl_pin   = Pin(pin_I2C_SCL, Pin.IN, Pin.PULL_UP)
sda_pin   = Pin(pin_I2C_SDA, Pin.IN, Pin.PULL_UP)

i2c = I2C(scl=scl_pin, sda=sda_pin, freq=50000)

### debug scan i2c-bus and print found devices
idev = i2c.scan()
print("idev= ", end='');
print(idev)
time.sleep_ms(200)

### attach to sensor
scd30 = SCD30(i2c, 0x61)
scd30.soft_reset()
time.sleep_ms(1000)

###
fw_version = scd30.get_firmware_version()
print("SCD30 Firmware Version: major=0x%02x minor=0x%02x" %  fw_version)

scd30.set_measurement_interval(2)
time.sleep_ms(100)

scd30.start_continous_measurement()
time.sleep_ms(100)

cnt = 0
start_time = utime.ticks_ms()
while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    while scd30.get_status_ready() != 1:
        time.sleep_ms(200)
    cnt += 1
    diff = utime.ticks_ms() - start_time
    print("%6d.%03d: " % (diff/1000,diff%1000), end = '')
    print("%3d, " % cnt, end = '')
    print(scd30.read_measurement())


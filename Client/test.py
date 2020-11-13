import time
from machine import I2C, Pin
from scd30 import SCD30

# Heltec LoRa32-board mit  OLED Display

i2c = I2C(0)
scd30 = SCD30(i2c, 0x61)

while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    while scd30.get_status_ready() != 1:
        time.sleep_ms(200)
    scd30.read_measurement()

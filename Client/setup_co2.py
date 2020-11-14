# make the co2-sensor ready to run continuously
#
from machine import Pin, I2C
from scd30 import SCD30
from machine_esp32_heltec_LoRa32 import *

def co2_attach():
    scl_pin_scd30   = Pin(pin_I2C_SCL, Pin.IN, Pin.PULL_UP)
    sda_pin_scd30   = Pin(pin_I2C_SDA, Pin.IN, Pin.PULL_UP)
    i2c_scd30 = I2C(scl=scl_pin_scd30, sda=sda_pin_scd30, freq=50000)

    ### debug scan i2c_scd30-bus and print found devices
    DEBUG = True
    if DEBUG:
        dev_scd30 = i2c_scd30.scan()
        print("idev= ", end='');
        print(idev_scd30)
        time.sleep_ms(200)

    ### attach to sensor
    scd30 = SCD30(i2c_scd30, 0x61)
    scd30.soft_reset()
    time.sleep_ms(1000)

    fw_version = scd30.get_firmware_version()
    print("SCD30 Firmware Version: major=0x%02x minor=0x%02x" %  fw_version)

    scd30.set_measurement_interval(2)
    time.sleep_ms(100)

    scd30.start_continous_measurement()
    time.sleep_ms(100)

    return scd30

#
print('\n### OpenPhotonik_Makeathon2020\n')

import time, utime
from time import sleep
# from machine import Pin, I2C

from machine_esp32_heltec_LoRa32 import *

# from rgb_led import *
# from ssd1306 import SSD1306_I2C

from setup_co2 import *
from scd30 import SCD30

scd30 = co2_attach()


from setup_oled import *
setup_oled()

from setup_rgb import *
setup_rgb()

########################################
### main loop
# 1. fetching sensor data
# 2. update oled
# 3. update rgb_led
# 4. update mqtt server

m_cnt = 0
m_err = 0
start_time = utime.ticks_ms()
while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    up_time = utime.ticks_ms() - start_time
    try:
        while scd30.get_status_ready() != 1:
            time.sleep_ms(200)
        m_cnt += 1
        result = scd30.read_measurement()
    except OSm_error:
        m_err += 1
        result = 'skipped'
    if m_err:
        m_quot = m_cnt/m_err
    else:
        m_quot = m_cnt
    print("%6d.%03d: " % (up_time/1000, up_time%1000), end = '')
    print("%3d/%3d/%3d, " % (m_cnt,m_err, m_quot), end = '')
    print( result )

    if result == "skipped":
        continue     # start while loop over again

    ### here we have a real value so we can updte the display and LED
    r_co2, r_temp, r_hum = result    # assign tupel to named variables
    r_co2 = int(r_co2)
    
    oled_update_co2(r_co2)
    rgb_led_update_co2(r_co2)
    # mqtt_update(r_co2, r_temp, r_hum)
    
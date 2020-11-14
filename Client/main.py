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

mqtt_client_prefix  = b'Hackaton-'
#mqtt_server         = b'mqtt.mydomain.lan'  # DNS name
mqtt_server         = b'192.168.1.58'       # IP-addr
from setup_mqtt import *
setup_mqtt(mqtt_server, mqtt_client_prefix)

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
    m_quot  = m_cnt
    try:
        while scd30.get_status_ready() != 1:
            time.sleep_ms(200)
        m_cnt += 1
        result = scd30.read_measurement()
    except OSError:
        m_err += 1
        m_quot = m_cnt/m_err
        result = 'skipped'
        
    print("%6d.%03d: " % (up_time/1000, up_time%1000), end = '')
    print("%3d/%3d/%3d, " % (m_cnt,m_err, m_quot), end = '')
    print( result )

    if result == "skipped":
        continue     # start while loop over again

    ### here we have a real value so we can updte the display and LED
    r_co2, r_temp, r_hum = result    # assign tupel to named variables
    r_co2  = int(r_co2)
    r_hum  = int(r_hum)       # datasheet 3% accuracy
    r_temp = int(r_temp*10) / 10  # only 0.1 accuracy should be enough

    oled_update_co2(r_co2)
    rgb_led_update_co2(r_co2)
    # mqtt-update
    mqtt_publish( b'/m_uptime', up_time )
    mqtt_publish( b'/m_cnt',    m_cnt )
    mqtt_publish( b'/m_err',    m_err )
    mqtt_publish( b'/m_quot',   m_quot )
    mqtt_publish( b'/co2',      r_co2 )
    mqtt_publish( b'/temp',     r_temp )
    mqtt_publish( b'/hum',      r_hum )
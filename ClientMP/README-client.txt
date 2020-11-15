# Client -- Heltec LoRa32-board with OLED Display
###---------------------------------------------------------------------------
https://heltec.org/project/wifi-lora-32/

# attached devices:
	- SDC30
	- RGB-LED

### Client using Micropython
###---------------------------------------------------------------------------
https://micropython.org/resources/firmware/esp32-idf3-20200902-v1.13.bin
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin

# developing and uploading python tools we used thonny ide 3.7.2
# using thonny or other tool to upload content of ClientMP/ to Heltec LoRa32-board with OLED Display
# upload :  ClientMP/lib dir and ALL Client/*.py

# WLAN config
###---------------------------------------------------------------------------
ClientMP/lib/wlan_mywlan.py	# change SSID/password to your needs

# WLAN enable/disable
ClientMP/boot.py		# set WLAN_ENABLE = True/False	default: True 

# MQTT
###---------------------------------------------------------------------------
https://micropython-iot-hackathon.readthedocs.io/en/latest/mqtt.html
https://pypi.org/project/micropython-umqtt.simple/


### TODO:
###---------------------------------------------------------------------------
- LoRa integration
- transmitt data over Lora (same data as mqtt)

PROBLEM: after ~6hours 
 21432.342: 10430/822/10429, (803.391, 23.88915, 43.46313)
 21434.517: 10431/822/10430, (803.5596, 23.88915, 43.42957)
 21436.497: 10432/822/10431, (803.4331, 23.9025, 43.41736)
 21438.677: 10433/822/10432, (803.1856, 23.91585, 43.4433)
 21440.651: 10434/822/10433, (802.4941, 23.88915, 43.41583)
 21442.623: 10435/822/10434, (802.9569, 23.9025, 43.42957)
 21444.795: 10436/822/10435, (802.9708, 23.9025, 43.45245)
Traceback (most recent call last):
  File "main.py", line 40, in <module>
  File "/lib/scd30.py", line 96, in get_status_ready
  File "/lib/scd30.py", line 166, in __check_crc
CRCException:
MicroPython v1.13 on 2020-09-02; ESP32 module with ESP32
Type "help()" for more information.


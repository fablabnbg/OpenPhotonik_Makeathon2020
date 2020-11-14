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

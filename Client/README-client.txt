# Client -- Heltec LoRa32-board mit  OLED Display
https://heltec.org/project/wifi-lora-32/

# attached devices:
	- SDC30
	- RGB-LED

# Client using Micropython

https://micropython.org/resources/firmware/esp32-idf3-20200902-v1.13.bin
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin

# developing and uploading python tools we used thonny ide 3.7.2

# WLAN config
lib/wlan_mywlan.py	# change SSID/password to your needs

# WLAN enable/disable
boot.py			#  un/comment: if True:   if False: around line 12-13


###---------------------------------------------------------------------------
### TODO:
test_co2.py		# after a while it stops due to timeout
Traceback (most recent call last):
  File "<stdin>", line 42, in <module>
  File "/lib/scd30.py", line 95, in get_status_ready
  File "/lib/scd30.py", line 161, in __read_bytes
OSError: [Errno 110] ETIMEDOUT

# Client -- Heltec LoRa32-board mit  OLED Display
# attached devices:
	- SDC30
	- RGB-LED

# Client using Micropython

https://micropython.org/resources/firmware/esp32-idf3-20200902-v1.13.bin
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin

# developing and uploading python tools we used thonny ide 3.7.2



#import LoRaDuplexCallback
#import LoRaPingPong
#import LoRaSender

#from config import *
from machine import Pin, SPI
from sx127x import SX127x
from LoRaSender import lorasender
#from LoRaReceiver import LoRaReceiver
#from ssd1306_i2c import Display
from time import sleep

device_config = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':14,
    'led':2, 
}

lora_parameters = {
    'frequency': 433E6, 
    'tx_power_level': 2, 
    'signal_bandwidth': 125E3,    
    'spreading_factor': 8, 
    'coding_rate': 5, 
    'preamble_length': 8,
    'implicit_header': False, 
    'sync_word': 0x12, 
    'enable_CRC': False,
    'invert_IQ': False,
}

device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)

example = 'sender'
#example = 'receiver'
if __name__ == '__main__':
    if example == 'sender':
        lorasender.send(lora);
        

# This file is executed on every boot (including wake-boot from deepsleep)
import esp
#esp.osdebug(None)
import uos, machine
import time

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc
import webrepl

if False:
    import wlan_wline2
    #import wlan_fln
    #
    # SSID: MicroPython-*
    # PASS: micropythoN
    # http://micropython.org/webrepl/
    webrepl.start()
gc.collect()

from hb import *
#from machine_esp32_wroom32 import *
#from machine_esp32_pico_kit_v4 import *
from machine_esp32_heltec_LoRa32 import *

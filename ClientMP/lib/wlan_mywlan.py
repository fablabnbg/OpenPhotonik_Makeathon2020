import network
import time

print('MYWLAN.setup')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'passwd')      # change here to your local WLAN params
for x in range(5):
    print('.', end='')
    time.sleep(1)
else:
    print('\nwlan.ifconfig: ', end='')
print(wlan.ifconfig())
print('MYWLAN.done')

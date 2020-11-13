import network
import time

print('FLN.setup')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('FLN', 'fablabnbg')
for x in range(5):
    print('.', end='')
    time.sleep(1)
else:
    print('\nwlan.ifconfig: ', end='')
print(wlan.ifconfig())
print('wline2.done')

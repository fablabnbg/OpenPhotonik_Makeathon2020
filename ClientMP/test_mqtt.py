#
# https://pypi.org/project/micropython-umqtt.simple/
# import upip
# upip.install('micropython-umqtt.simple')
# 
# This test expect existing wifi connection
#
####################################### #######################################

from umqtt.simple import MQTTClient
import ubinascii
import machine

def my_mqtt_init(server, id_client):
    id = id_client + ubinascii.hexlify(machine.unique_id()[3:])
    c = MQTTClient(id_client, server)
    c.connect()
    return c, id

def my_mqtt_stop(mc):
    mc.disconnect()

def my_mqtt_test(id_prefix, server_url):
    mc, mc_id = my_mqtt_init(server_url, id_prefix)
    print('server   : %s' % server_url)
    print('id_prefix: %s' % id_prefix)
    print('mc_id    : %s' % mc_id)

    mc.publish(mc_id + b"/sensor1", b'123')
    mc.publish(mc_id + b"/sensor2", b'234')
    my_mqtt_stop(mc)
    

####################################### #######################################
### main
if __name__ == '__main__':
    client_prefix  = b'Hackaton-'
    my_mqtt_server = b'192.168.1.58'
    my_mqtt_test(client_prefix, my_mqtt_server)

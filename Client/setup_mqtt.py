#
# expect existing wifi connection
####################################### #######################################

from umqtt.simple import MQTTClient
import ubinascii
import machine

mc    = None
mc_id = None

def setup_mqtt(server_url, client_prefix):
    global mc
    global mc_id
    mc, mc_id = my_mqtt_init(server_url, client_prefix)


def mqtt_publish( sensor_path, sensor_value ):
    value = bytes(str(sensor_value), 'ascii' )
    mc.publish(mc_id + sensor_path, value)

############################
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
    


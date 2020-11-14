#/bin/sh
#
#
# config:
# sudo crontab -e
# add: @reboot sh /home/pi/IOTstack/bin/launcher.sh >/home/pi/IOTstack/LOGS/cronlog 2>&1
# 
set -euo	# stop script on error


echo "### $0"
sleep 60
export USER_DIR="/home/pi"
export IOTSTACK_DIR="$USER_DIR/IOTstack"
export LOG_DIR="$IOTSTACK_DIR/LOGS"

### MAIN
cd /
cd $USER_DIR
mkdir -p LOGS 2>&1 > /dev/null

### start MQTT to INFLUX bridge
cd $IOTSTACK_DIR
sudo python3 bin/MQTTInfluxDBBridge.py >$LOG_DIR/MQTTInfluxDBBridge.log 2>&1 &

cd /

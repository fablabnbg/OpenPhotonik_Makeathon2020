### use raspberry pi 4 as the central server.

# links:
https://www.youtube.com/watch?v=a6mjt8tWUws	# Check this first
Software and instructions: http://www.iotStack.org
https://diyi0t.com/visualize-mqtt-data-with-influxdb-and-grafana/	# setup description

### after basic setup
# install:
- Portainer-ce
- Node-RED
- InfluxDB
  portainer console login
  influx
  	CREATE DATABASE Makeathon
  	use Makeathon
	CREATE USER mqtt WITH PASSWORD 'mqttSafe'
	GRANT ALL ON Makeathon TO mqtt
	exit
  sudo apt install python3-pip
  sudo apt install python3-paho-mqtt	# OR sudo pip3 install paho-mqtt
  sudo apt install python3-influxdb	# OR sudo pip3 install influxdb

- Grafana
- Eclipse-Mosquitto



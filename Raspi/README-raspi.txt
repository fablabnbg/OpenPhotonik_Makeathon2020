### use raspberry pi 4 as the central server.

# links:
https://www.youtube.com/watch?v=a6mjt8tWUws	# Check this first
Software and instructions: http://www.iotStack.org
https://diyi0t.com/visualize-mqtt-data-with-influxdb-and-grafana/	# setup description

### after basic setup
# install:
- Portainer-ce
- Node-RED
- Eclipse-Mosquitto
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
  rsync -av Raspi/IOTstack/   pi@raspi:~/IOTstack/
  read and config as described in ~/IOTstack/launcher.sh

- Grafana
  browser: http:raspi:3000
  	username: admin
  	password: admin
	change password
	on the left side configuration -> datasources
		OR http://pi4:3000/datasources
		add datasource - select influxdb
		change URL:  http://192.168.1.58:8086		# use ip addr from raspi
		change Database: Makeathon
		user:   mqtt
		passwd: mqttSafe
	left menu panel you can choose the “Explore” button
		see: grafana setup https://diyi0t.com/visualize-mqtt-data-with-influxdb-and-grafana/




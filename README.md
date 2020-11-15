# OpenPhotonik_Makeathon2020
Make-athon von OpenPhotonic, November 2020

This is a project:
- Uses an ESP32 with Micropython to implement:
  - OLED-display to display measured data co2 / temp / humity
  - RGB-LED for traffic light indication
  - uses wifi connection to
    - upload measured data to MQTT-server
- Uses a RASPI4 with IOTstack working as a server
 - influxdb as a database to store measured data from all sensor-nodes
 - grafana for visualize the measured data
 - NodeRed to provide a dashbaord for a quick overview of all sensor-nodes
 
- OPEN (not implemented)
  - sending data over LoRa

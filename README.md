Are you having problems with gray Herons on your pond?
The container monitors your area, using an IP Camera and when 
a Heron is identified, there is an alarm about Mqtt.

Necessary components:
Raspberry Pi >= 4 with Docker
IP camera (with zoom is an advantage)
Mqtt client, like ioBroker etc.
Optional:
Coral Edge TPU USB

Steps:
Create directories on the Docker host
mkdir docker/tflite # Volume for the container
mkdir coral # Paste the repo files here
Edit the script reiher.py

cd coral
docker build -t "reiher" .
docker run -it --privileged --restart always -e MTX_PROTOCOLS=tcp -v /dev/bus/usb:/dev/bus/usb -v /home/pi/docker/tflite:/tflite reiher /bin/bash

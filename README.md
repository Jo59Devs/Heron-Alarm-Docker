Alarm when a gray heron is at your pond<br />
The container monitors your area, using an IP Camera and when <br />
a Heron is identified, there is an alarm about Mqtt.<br />

Necessary components:<br />
Raspberry Pi >= 4 with Docker<br />
IP camera (with zoom is an advantage)<br />
Mqtt client, like ioBroker etc.<br />
Optional:<br />
Coral Edge TPU USB<br />

Steps:<br />
Create directories on the Docker host<br />
mkdir docker/tflite # Volume for the container<br />
mkdir coral # Paste the repo files here<br />
Edit the script reiher.py<br />

cd coral<br />
docker build -t "reiher" .<br />
docker run -it --privileged --restart always -e MTX_PROTOCOLS=tcp -v /dev/bus/usb:/dev/bus/usb -v /home/pi/docker/tflite:/tflite reiher /bin/bash<br />

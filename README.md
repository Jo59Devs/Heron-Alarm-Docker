<h1>Heron Alarm at the Pond</h1>

The Docker container monitors your pond.<br/>
If a heron is detected, an alarm is triggered via MQTT.<br/>

Required components:<br/>
<ul>Raspberry Pi >= 4<br/>
Installed Docker<br/>
IP Camera (with zoom an advantage)<br/>
MQTT Client, such as ioBroker, etc.<br/>
Optional:<br/>
Coral Edge TPU USB Accelerator - around 50 frames/s on Raspberry Pi 4, without it approximately 7 frames/s</ul><br/>

Steps:<br/>
<ul><li>Create the following paths on the Docker host:<li><br/>
<code>mkdir docker/tflite</code> # Volume for the container<br/>
<code>mkdir coral</code> # Add the repository files here<br/>
Edit <code>reiher.py</code><br/>
Adjust your MQTT client<br/>
Change the MQTT alarm ID<br/>
Change the RTSP link of your camera<br/>
Choose whether to use the Edge TPU accelerator or not</ul><br/>

<code>cd coral<br/>
docker build -t "reiher".
docker run -it --privileged --restart always \\
    -e MTX_PROTOCOLS=tcp \\
    -v /dev/bus/usb:/dev/bus/usb \\
    -v /home/pi/docker/tflite:/tflite \\
    reiher /bin/bash</code>

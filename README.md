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
<ul>Create the following paths on the Docker host:<br/>
<li><code>mkdir docker/tflite</code> # Volume for the container</li>
<li><code>mkdir coral</code> # Add the repository files here</li>
<li>Edit <code>reiher.py</code></li><br/>
<li>Adjust your MQTT client</li><br/>
<li>Change the MQTT alarm ID</li><br/>
<li>Change the RTSP link of your camera</li><br/>
<li>Choose whether to use the Edge TPU accelerator or not</li></ul><br/>

<code>cd coral<br/>
docker build -t "reiher".
docker run -it --privileged --restart always \\
    -e MTX_PROTOCOLS=tcp \\
    -v /dev/bus/usb:/dev/bus/usb \\
    -v /home/pi/docker/tflite:/tflite \\
    reiher /bin/bash</code>

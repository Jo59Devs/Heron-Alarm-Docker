<h1>Heron Alarm at the Pond</h1>

The Docker container monitors your pond.<br/>
If a heron is detected, an alarm is triggered via MQTT.<br/>

Required components:<br/>
<ul><li>Raspberry Pi >= 4</li>
<li>Installed Docker</li>
<li>IP Camera (with zoom an advantage)</li>
<li>MQTT Client, such as ioBroker, etc.</li></ul>
Optional:
<ul><li>Coral Edge TPU USB Accelerator - ≈50 frames/s on Pi 4, without ≈7 frames/s</li></ul>

Steps:<br/>
<ul><li><code>mkdir docker/tflite</code> # Volume for the container</li>
<li><code>mkdir coral</code> # Add the repository files here</li>
<li>Edit <code>reiher.py</code></li>
<li>Adjust your MQTT client</li>
<li>Change the MQTT alarm ID</li>
<li>Change the RTSP link of your camera</li>
<li>Choose whether to use the Edge TPU accelerator or not</li></ul><br/>

<code>cd coral<br/>
docker build -t "reiher".
docker run -it --privileged --restart always \\
    -e MTX_PROTOCOLS=tcp \\
    -v /dev/bus/usb:/dev/bus/usb \\
    -v /home/pi/docker/tflite:/tflite \\
    reiher /bin/bash</code>

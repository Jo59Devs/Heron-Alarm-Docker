<h1>Alarm: Reiher am Teich</h1>

Der Docker-Container überwacht ihren Teich.<br/>
Wird ein Reiher identifiziert, gibt es einen Alarm über MQTT.<br/>

Notwendige Komponenten:<br/>
Raspberry Pi >= 4<br/>
IP Kamera (mit Zoom ist von Vorteil)<br/>
MQTT-Client, wie ioBroker etc.<br/>
Optional:<br/>
Coral Edge TPU USB Accelerator - ca. 50 frames/s auf dem Raspberry Pi 4, ohne ca. 7 frames/s<br/>

Schritte:<br/>
Erstellen sie folgende Pfade auf dem Docker Host:<br/>
<code>mkdir docker/tflite</code> # Volume für den Container<br/>
<code>mkdir coral</code> # Hier die Repo Dateien einfügen<br/>

Editieren von reiher.py<br/>
Passen sie ihren MQTT-Client an<br/>
Ändern sie die MQTT Alarm-ID<br/>
Ändern sie den RTSP-Link ihrer Kamera<br/>
Wählen sie mit oder ohne Edge TPU Accelerator<br/>

<code>cd coral</code><br/>
docker build -t "reiher".</code><br/>
docker run -it --privileged --restart always \<br/>
    -e MTX_PROTOCOLS=tcp \<br/>
    -v /dev/bus/usb:/dev/bus/usb \<br/>
    -v /home/pi/docker/tflite:/tflite \<br/>
    reiher /bin/bash</code><br/>

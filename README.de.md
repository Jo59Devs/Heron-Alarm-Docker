<h1>Reiher Alarm am Teich</h1>

Der Docker Container überwacht ihren Teich.<br/>
Wenn ein Reiher im Bereich ist, wird ein Alarm via MQTT ausgelöst.<br/>
Zudem wird ein Bild im Image-Ordner gespeichert.<br/>

Benötigte Komponenten:<br/>
<ul><li>Raspberry Pi >= 4</li>
<li>Installierter Docker</li>
<li>IP Kamera (mit Zoom von Vorteil)</li>
<li>MQTT Client, wie ioBroker, etc.</li></ul>
Optional:
<ul><li>Coral Edge TPU USB Accelerator - ≈50 frames/s auf Pi 4, ohne ≈7 frames/s</li></ul>

Ordner anlegen:<br/>
<ul><li><code>mkdir docker/tflite</code> # Volume für den Container</li>
<li><code>mkdir coral</code> # Hier die Repo Dateien einfügen</li></ul>
Bearbeiten von <code>heron.py</code>
<ul><li>Anpassen des MQTT client</li>
<li>Ändern der MQTT Alarm ID</li>
<li>RTSP-Link der Kamera anpassen</li>
<li>Auswahl ob mit oder ohne Edge TPU Accelerator</li></ul><br/>

<h3>Erstellen des Containers:</h3>
<pre style="background-color: #f4f4f4; border: 1px solid #ddd; border-radius: 5px; padding: 10px; color: #333; font-family: 'Courier New', Courier, monospace; line-height: 1.5;">
<span style="color: #0000ff;">cd</span> coral
<span style="color: #0000ff;">docker</span> build -t <span style="color: #a31515;">"heron"</span>.
<span style="color: #0000ff;">docker</span> run -it --privileged --restart always \
    -e MTX_PROTOCOLS=<span style="color: #a31515;">tcp</span> \
    -v <span style="color: #a31515;">/dev/bus/usb:/dev/bus/usb</span> \
    -v <span style="color: #a31515;">/home/pi/docker/tflite:/tflite</span> \
    heron /bin/bash
</pre>
Anmerkung: Teile des Python-Script stammen aus der original Google-Coral Repo

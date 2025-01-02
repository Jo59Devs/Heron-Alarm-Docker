<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reiher-Alarm</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }
        h1 {
            font-size: 1.8em;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 1.5em;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        code {
            display: block;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.95em;
            overflow-x: auto;
        }
        .italic {
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Alarm: <span class="italic">Reiher am Teich</span></h1>
    <p>Der Docker-Container überwacht Ihren Teich.<br>
    Wird ein Reiher identifiziert, gibt es einen Alarm über MQTT.</p>

    <h2>Notwendige Komponenten:</h2>
    <ul>
        <li>Raspberry Pi &ge; 4</li>
        <li>IP Kamera (mit Zoom ist von Vorteil)</li>
        <li>MQTT-Client, wie ioBroker etc.</li>
        <li>Optional:
            <ul>
                <li>Coral Edge TPU USB Accelerator - ca. 50 frames/s auf dem Raspberry Pi 4, ohne ca. 7 frames/s</li>
            </ul>
        </li>
    </ul>

    <h2>Schritte:</h2>
    <ol>
        <li>Erstellen Sie folgende Pfade auf dem Docker Host:</li>
        <code>
            mkdir docker/tflite <span class="italic"># Volume für den Container</span><br>
            mkdir coral <span class="italic"># Hier die Repo Dateien einfügen</span>
        </code>
        <li>Editieren Sie die Datei <code>reiher.py</code>:</li>
        <ul>
            <li>Passen Sie Ihren MQTT-Client an.</li>
            <li>Ändern Sie die MQTT-Alarm-ID.</li>
            <li>Ändern Sie den RTSP-Link Ihrer Kamera.</li>
            <li>Wählen Sie mit oder ohne Edge TPU Accelerator.</li>
        </ul>
        <li>Erstellen Sie den Container:</li>
        <code>
            cd coral<br>
            docker build -t "reiher".<br>
            docker run -it --privileged --restart always -e MTX_PROTOCOLS=tcp -v /dev/bus/usb:/dev/bus/usb -v /home/pi/docker/tflite:/tflite reiher /bin/bash
        </code>
    </ol>
</body>
</html>

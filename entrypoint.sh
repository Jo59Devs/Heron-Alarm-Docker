#!/bin/bash

# Prüfe, ob das Host-Verzeichnis bereits Dateien enthält
if [ ! -f /tflite/reiher.py ]; then
    echo "Initialisiere Host-Verzeichnis mit Dateien aus dem Container..."
    cp -r /root/tmp/* /tflite
else
    echo "Host-Verzeichnis ist bereits initialisiert."
fi

# Wechsel in das Arbeitsverzeichnis
cd /tflite

# Starte den Hauptprozess
echo "Starte Hauptprozess: reiher.py"
exec python3 reiher.py

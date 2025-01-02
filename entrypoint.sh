#!/bin/bash

# Check if the host directory already contains files
if [ ! -f /tflite/reiher.py ]; then
    echo "Initialize host directory with files from container..."
    mv /tmp/reiher.py /tflite/reiher.py
else
    echo "Host directory is already initialized."
fi
# Start the main process
echo "Start the main process: reiher.py"
exec python3 /tflite/reiher.py

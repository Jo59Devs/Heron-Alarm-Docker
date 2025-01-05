#!/bin/bash

# Check if the host directory already contains files
if [ ! -f /tflite/heron.py ]; then
    echo "Initialize host directory with files from container..."
    mv /tmp/heron.py /tflite/heron.py
else
    echo "Host directory is already initialized."
fi
# Start the main process
echo "Start the main process: heron.py"
exec python3 /tflite/heron.py

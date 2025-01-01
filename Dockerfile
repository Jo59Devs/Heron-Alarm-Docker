FROM debian:bullseye
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install nano -y
RUN apt-get install python3-pip -y
RUN apt-get install python-dev -y
RUN apt-get install pkg-config -y
RUN apt-get install wget -y
RUN apt-get install usbutils -y
RUN apt-get install curl -y
RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" \
| tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update
RUN apt-get install libedgetpu1-std
RUN apt-get install python3-pycoral -y
RUN pip3 install tflite-runtime
RUN pip3 install --upgrade pip
RUN apt-get install python3-opencv -y
RUN pip3 install imutils
RUN pip3 install paho-mqtt
RUN pip3 install -U numpy==1.23.5
RUN pip3 install pillow
RUN apt-get install -y libatlas-base-dev
WORKDIR /root/tmp
RUN mkdir -p image models && \
    curl -o models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite \
        https://github.com/google-coral/edgetpu/raw/master/test_data/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite && \
    curl -o models/mobilenet_v2_1.0_224_inat_bird_quant.tflite \
        https://github.com/google-coral/edgetpu/raw/master/test_data/mobilenet_v2_1.0_224_inat_bird_quant.tflite && \
    curl -o models/inat_bird_labels.txt \
        https://github.com/google-coral/edgetpu/raw/master/test_data/inat_bird_labels.txt
COPY reiher.py .
RUN chmod +x /root/tmp/entrypoint.sh
ENTRYPOINT ["/root/tmp/entrypoint.sh"]

#docker run -it --privileged --restart always -e MTX_PROTOCOLS=tcp -v /dev/bus/usb:/dev/bus/usb -v /home/pi/docker/tflite:/tflite --net=host reiher /bin/bash

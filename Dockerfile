FROM debian:bullseye
RUN apt-get update
RUN apt-get update && apt-get install -y \
    git \
    nano \
    python3-pip \
    python-dev \
    pkg-config \
    wget \
    usbutils \
    curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" \
| tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

RUN apt-get update && apt-get install -y \
    libedgetpu1-std \
    python3-pycoral \
    libatlas-base-dev \
    python3-opencv
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir \
    tflite-runtime \
    requests \
    imutils \
    paho-mqtt \
    numpy \
    pillow
WORKDIR /tmp
COPY heron.py entrypoint.sh .
RUN chmod +x entrypoint.sh
WORKDIR /tflite
ENTRYPOINT ["/tmp/entrypoint.sh"]

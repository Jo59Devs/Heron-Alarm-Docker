import os
import sys
import cv2
import time
import signal
import datetime
import numpy as np
from os import path
import importlib.util
import paho.mqtt.client as mqtt
from imutils.video import VideoStream, FPS
from PIL import Image, ImageDraw, ImageFont
from tflite_runtime.interpreter import Interpreter, load_delegate
# Edge-TPU
EDGETPU_SHARED_LIB = 'libedgetpu.so.1'
# Heron Classes
nval = [ 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.00, 0.00, 0.03, 0.01, 0.01, 0.50, 0.00]
list = [   13,   61,  559,  560,  561,  563,  564,  566,  567,  572,  592,  604,  765]

# Container Stop
def handle_signal(signum, frame):
    global client
    print(f"Signal {signum} empfangen.")
    client.disconnect()
    client.loop_stop()
    sys.exit(0)

# Heron Alarm
def send_alarm(image):
    global client
    stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    cv2.imwrite("/tflite/python/examples/classification/image/"+stamp+"-Reiher.jpg", image)
    client.publish("mqtt.0.Yard.Heron", 'true')

def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image

def classify_image(interpreter, image, top_k=4):
    """Returns a sorted array of classification results."""
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    output = np.squeeze(interpreter.get_tensor(output_details['index']))

    # If the model is quantized (uint8 data), then dequantize the results
    if output_details['dtype'] == np.uint8:
        scale, zero_point = output_details['quantization']
        output = scale * (output - zero_point)

    ordered = np.argpartition(-output, top_k)
    return [(i, output[i]) for i in ordered[:top_k]]


def draw_image(cnt, image, results, labels):
    draw = ImageDraw.Draw(image)
    for i0 in range(0, len(results)):
        for i1 in range(len(list)):
            if int(results[i0][0] == list[i1]) and results[i0][1] > nval[i1]:
                cnt += 1
                position = (5, (cnt*24)-15)
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 24)
                text = "{} {}: {:.2f}%".format(results[i0][0], labels[results[i0][0]], results[i0][1] * 100)
                bbox = draw.textbbox(position, text, font=font)
                draw.rectangle(bbox, fill="black")
                draw.text(position, text, font=font, fill="white")
    if cnt >= 3:
        displayImage = np.asarray(image)
        send_alarm(displayImage)

def load_labels(path, encoding='utf-8'):
    with open(path, 'r', encoding=encoding) as f:
        lines = f.readlines()
        if not lines:
            return {}

        if lines[0].split(' ', maxsplit=1)[0].isdigit():
            pairs = [line.split(' ', maxsplit=1) for line in lines]
            return {int(index): label.strip() for index, label in pairs}
        else:
            return {index: line.strip() for index, line in enumerate(lines)}

def make_interpreter(use_TPU):
    if use_TPU:
        model_file = 'models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite'
        model_file, *device = model_file.split('@')
        return Interpreter(model_path=model_file, experimental_delegates=[load_delegate(EDGETPU_SHARED_LIB, {'device': device[0]} if device else {})])
    else:
        model_file = 'models/mobilenet_v2_1.0_224_inat_bird_quant.tflite'
        model_file, *device = model_file.split('@')
        return Interpreter(model_path=model_file)

# MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "rpi-reiher")
client.username_pw_set("esp", "myesp")
client.connect("192.168.178.70", 1883, 60)
client.loop_start()

def main():
    global client
    # Register Signal-Handler
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)  # Optional für Ctrl+C in Entwicklung
    # Prepare labels.
    labels = load_labels('models/inat_bird_labels.txt')
    # Get interpreter
    # Without EdgeTPU !
    #interpreter = make_interpreter('')
    # With EdgeTPU
    interpreter = make_interpreter('edgetpu')
    interpreter.allocate_tensors()
    _, height, width, _ = interpreter.get_input_details()[0]['shape']
    # Initialize video stream
    cam = "rtsp://admin:touring@192.168.178.58:554//h264Preview_01_sub"
    vs = VideoStream(cam).start()
    # Waiting for Camera and Network
    time.sleep(4)
    while True:
        # Read frames from video
        screenshot = vs.read()
        if screenshot is not None:
            image = Image.fromarray(screenshot)
            # Perform inference
            image_pred = image.resize((width ,height), Image.LANCZOS)
            results = classify_image(interpreter, image_pred)
            draw_image(0, image, results, labels)
        # Reduce CPU-Acuracy
        time.sleep(0.04)

if __name__ == '__main__':
    main()
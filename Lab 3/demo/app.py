import eventlet
eventlet.monkey_patch()

from flask import Flask, Response,render_template
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call

import time
import board
import busio
# import adafruit_mpu6050
# from adafruit_msa3xx import MSA311
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3
import json
import socket

import signal
import sys
from queue import Queue

print("Digital IO ok!")
import smbus
bus = smbus.SMBus(1)
for address in range(0x08, 0x78):
    try:
        # Try to read a byte from the current address
        bus.read_byte(address)
        print(f"Device found at address: 0x{hex(address)}")
    except:
        pass
 
i2c = busio.I2C(board.SCL, board.SDA)

print("I2C ok!")
sox_add = 0x6a
sox = LSM6DS3(i2c, sox_add)
# mpu = adafruit_mpu6050.MPU6050(i2c, mpu_add)
# if (not mpu.begin()):
#   print("Failed to find MPU6050 chip")
# msa = MSA311(i2c, mpu_add)
print('SOX OK')

hostname = socket.gethostname()
hardware = 'plughw:1,0'

app = Flask(__name__)
socketio = SocketIO(app)
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)

@socketio.on('speak')
def handel_speak(val):
    call(f"espeak '{val}'", shell=True)

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-gps')
def handle_message(val):
    # print(mpu.acceleration)
    emit('pong-gps', sox.acceleration) 
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(sox.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s"%(sox.gyro))
    # print(sox.acceleration)



@app.route('/')
def index():
    return render_template('index.html', hostname=hostname)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)



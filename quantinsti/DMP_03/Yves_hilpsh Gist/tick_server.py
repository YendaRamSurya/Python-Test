#
# Simple Tick Data Server
#
import time
import random
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:5555')

SYMBOL = 100.

while True:
    SYMBOL += random.gauss(0, 1) / 2
    msg = f'SYMBOL {SYMBOL:.3f}'
    socket.send_string(msg)
    print(msg)
    time.sleep(random.random() * 2)

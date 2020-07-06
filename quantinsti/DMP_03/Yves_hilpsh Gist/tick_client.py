#
# Simple Tick Data Client
#
import zmq
import datetime as dt

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    msg = socket.recv_string()
    t = dt.datetime.now()
    print(str(t) + '| ' + msg)

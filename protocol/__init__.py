"""
Implementation of signal protocol.
Version: 0.0.1


Specification:
Header
version, UID, channels, compression, rate, timestamp, timeout

Data
timestamp, index, [signals,...],

"""
import socket
import struct
import ujson
import uuid
import time


HOST = socket.gethostname()
PORT = 12345
IP = '127.0.0.1'


HEADER = {
    'data': 'ack',
    'version': 0.01,
    'uid': str(uuid.uuid4()),
    'rate': 120,
    'compression': 0,
    'channels': 1,
    'timestamp': int(time.time()),
    'timeout': 20,
}

DATA = {
    'data': 'sig',
    'latency': 0,
    'index': 0,
    'signals': []
}

f2b = lambda f: struct.pack('f', f)
b2f = lambda b: struct.unpack('f', b)[0]
jload = lambda j: ujson.loads(j)
jdump = lambda d: ujson.dumps(d)

# TODO: use Cython structs
"""
Implementation of signal protocol.
Version: 0.0.1


Specification:
Header
data, version, UID, rate, compression, channels, timestamp, timeout

Data
data, latency, index, [signals,...],

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


class Header(object):
    def __init__(self, header):
        self.data = header.get('data')
        self.version = header.get('version')
        self.uid = header.get('uid')
        self.rate = header.get('rate')
        self.compression = header.get('compression')
        self.channels = header.get('channels')
        self.timestamp = header.get('timestamp')
        self.timeout = header.get('timeout')


class Signal(object):
    def __init__(self, signal):
        self.signals = signal.get('signals')
        self.index = signal.get('index')
        self.data = signal.get('data')
        self.latency = signal.get('latency')

    def channel(self, number):
        if number < self.channels:
            return self.signals[number]

    @property
    def channels(self):
        return len(self.signals)

f2b = lambda f: struct.pack('f', f)
b2f = lambda b: struct.unpack('f', b)[0]
jload = lambda j: ujson.loads(j)
jdump = lambda d: ujson.dumps(d)

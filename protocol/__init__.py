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


HEADER = {
    'version': 0.01,
    'uid': str(uuid.uuid4()),
    'rate': 120,
    'compression': 0,
    'channels': 1,
    'timestamp': int(time.time()),
    'timeout': 20,
}

DATA = {
    'distance': 0,
    'index': 0,
    'signals': []
}

f2b = lambda f: struct.pack('f', f)
b2f = lambda b: struct.unpack('f', b)[0]
jload = lambda j: ujson.loads(j)
jdump = lambda d: ujson.dumps(d)


class Server(object):
    def __init__(self, ):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20)
        self.address = None
        self.header = HEADER
        self.distance = time.time()
        self.index = 0

    def ack(self):
        self.server.sendto(jdump(self.header), (HOST, PORT))

    def transfer(self, msg):
        self.server.sendto(self.payload(msg), (HOST, PORT))

    def payload(self, signals):
        self.index += 1
        now = time.time()
        distance = now - self.distance
        self.distance = now
        return jdump({'signals': signals, 'index': self.index, 'distance': distance})

    def close(self):
        self.server.close()


class Client(object):
    def __init__(self):
        self.buf_size = 1024
        self.acked = False
        self.addr = None
        self.header = HEADER

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
            print 'Some systems do not support SO_REUSEPORT'
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)
        self.client.bind(('', PORT))
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(socket.gethostbyname(HOST)))

    def ack(self):
        self.acked = False
        while not self.acked:
            self.header.update(self.listen().next())
            if self.header:
                self.acked = True
                print 'Acknowledged - Header: ', self.header
                self.acked = True
            else:
                print 'Try again..'

    def listen(self):
        while True:
            msg, self.addr = self.client.recvfrom(self.buf_size)
            msg = jload(msg)
            if msg:
                yield msg

            if msg in ['off']:
                break

    def close(self):
        self.client.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP,
                               socket.inet_aton(self.addr) + socket.inet_aton('0.0.0.0'))
        self.client.close()


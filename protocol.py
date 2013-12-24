"""
Implementation of signal protocol.
Version: 0.0.1


Specification:
Header
version, UID, rate, timestamp, compression, timeout

Data
timestamp, index, channels, [signals,...],

"""
import socket
import struct
import ujson


HOST = socket.gethostname()
PORT = 12345

HEADER = ['version', 'uid', 'rate', 'timestamp', 'compression', 'timeout']
DATA = {'timestamp': 0, 'index': 0, 'channels': 0, 'signals': []}

f2b = lambda f: struct.pack('f', f)
b2f = lambda b: struct.unpack('f', b)[0]


class Server(object):
    def __init__(self):
        self.server = socket.socket()
        self.server.bind((HOST, PORT))
        self.connection = None
        self.address = None

    def listen(self):
        self.server.listen(5)
        while not self.connection:
            self.connection, self.address = self.server.accept()
        print 'Connected to %s : %s' % self.address

    def ack(self):
        self.transfer(ujson.dumps(HEADER))

    def transfer(self, msg):
        self.connection.send(msg)

    def close(self):
        self.connection.close()


class Client(object):
    def __init__(self, header):
        self.client = socket.socket()
        self.client.connect((HOST, PORT))
        self.block = 4
        self.acked = False
        self.header = header

    def ack(self):
        msg = ujson.loads(self.receive(10).next())
        if msg in self.header:
            self.acked = True
            print 'Acknowledged.'
        else:
            print 'Try again..'

    def receive(self, block=None):
        block = block or self.block
        while True:
            msg = self.client.recv(block)
            if not msg:
                print 'No more msg.'
                break
            else:
                yield msg

    def close(self):
        self.client.close()


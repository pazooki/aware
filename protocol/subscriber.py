import zmq
from definition import *


class Subscriber(object):
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect('tcp://%s:%s' % (IP, PORT))
        self.socket.setsockopt(zmq.SUBSCRIBE, '')
        # self.socket.setsockopt(zmq.SUBSCRIBE, 'meta')
        # self.socket.setsockopt(zmq.SUBSCRIBE, 'signal')
        self.header = HEADER

    def listen(self):
        while True:
            print 'listening'
            msg = self.socket.recv()
            yield msg

    def close(self):
        print 'Closing time..'
        self.socket.close()

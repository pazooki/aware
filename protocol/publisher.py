import zmq
from definition import *


class Publisher(object):
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.latency = time.time()
        self.index = 0
        self.header = HEADER

    def open(self):
        self.socket.bind('tcp://*:%s' % PORT)
        self.meta({'status': 'open', 'header': self.header})

    def close(self):
        self.meta({'status': 'close', 'header': self.header})
        self.socket.close()

    def meta(self, data):
        outgoing = 'meta %s' % jdump(data)
        print outgoing
        self.socket.send(outgoing)

    def publish(self, data):
        outgoing = 'signal %s' % self.payload(data)
        print outgoing
        self.socket.send(data=outgoing, flags=zmq.NOBLOCK)

    def payload(self, signals):
        self.index += 1
        return jdump({'signals': signals, 'index': self.index, 'latency': self._latency})

    @property
    def _latency(self):
        now = time.time()
        latency = now - self.latency
        self.latency = now
        return latency

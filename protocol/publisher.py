# TODO: syncronizer should become the parent process for publisher

import zmq
from definition import *


class Publisher(object):
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.set_hwm(100)
        self.latency = time.time()
        self.index = 0
        self.header = HEADER

    def open(self):
        self.socket.bind('tcp://*:%s' % PORT)

    def ack(self):
        syncservice = self.context.socket(zmq.REP)
        syncservice.bind('tcp://*:5562')
        synced = False
        while not synced:
            msg = jload(syncservice.recv())
            if msg.get('status') in ['synchnorize']:
                syncservice.send('meta %s' % jdump(
                    {'status': 'synchnorize', 'header': self.header}
                ))
                synced = True
        self.meta({'status': 'open', 'header': self.header})

    def close(self):
        self.meta({'status': 'close', 'header': self.header})
        self.socket.close()

    def meta(self, data):
        outgoing = 'meta %s' % jdump(data)
        self.socket.send(outgoing)

    def publish(self, data):
        outgoing = 'signal %s' % self.payload(data)
        print outgoing
        self.socket.send(data=outgoing, flags=zmq.NOBLOCK)

    def payload(self, signals):
        self.index += 1
        return jdump({'signals': signals, 'index': self.index,
                      'latency': self._latency, 'ts': time.time()})

    @property
    def _latency(self):
        now = time.time()
        latency = now - self.latency
        self.latency = now
        return latency

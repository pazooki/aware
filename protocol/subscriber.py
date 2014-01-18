import zmq
from definition import *


class Subscriber(object):
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect('tcp://%s:%s' % (IP, PORT))
        self.socket.setsockopt(zmq.SUBSCRIBE, 'meta')
        self.socket.setsockopt(zmq.SUBSCRIBE, 'signal')
        self.header = HEADER
        self.synced = False

    def ack(self):
        syncclient = self.context.socket(zmq.REQ)
        syncclient.connect('tcp://localhost:5562')
        syncclient.send(jdump({'status': 'synchnorize', 'header': self.header}))
        self.synced = self.process(syncclient.recv())
        self.listen()

    def listen(self):
        while self.synced:
            data = self.process(self.socket.recv())
            if data in ['closed']:
                break
            elif data in ['opened']:
                pass
            elif data:
                yield data

    def process(self, msg):
        topic, data = msg.split()
        if topic in ['meta']:
            return self.meta(jload(data))
        elif topic in ['signal']:
            return jload(data)

    def meta(self, data):
        result = getattr(self,
                         data.get('status'),
                         lambda x: False)(data.get('header'))
        if not result:
            print '%s() is not available.' % data.get('status')
            return False
        else:
            return result

    def synchnorize(self, header):
        return True

    def open(self, header):
        print 'Opened connection..'
        return 'opened'

    def close(self, header):
        print 'Closed connection..'
        self.socket.close()
        self.synced = False
        return 'closed'

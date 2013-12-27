from protocol import *


class Server(object):
    def __init__(self, ):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20)
        self.address = None
        self.header = HEADER
        self.latency = time.time()
        self.index = 0

    def ack(self):
        self.server.sendto(jdump(self.header), (HOST, PORT))

    def transfer(self, data, msg):
        self.server.sendto(self.payload(data, msg), (HOST, PORT))

    def payload(self, data, signals):
        self.index += 1
        return jdump({'data': data, 'signals': signals, 'index': self.index, 'latency': self._latency})

    def close(self):
        self.transfer('off', [])
        self.server.close()

    @property
    def _latency(self):
        now = time.time()
        latency = now - self.latency
        self.latency = now
        return latency

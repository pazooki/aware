from protocol import *

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
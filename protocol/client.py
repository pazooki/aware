from protocol import *


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

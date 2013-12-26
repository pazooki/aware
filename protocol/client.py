from protocol import *


class Client(object):
    def __init__(self):
        self.buf_size = 1024
        self.acked = False
        self.addr = None
        self.header = HEADER
        self.intf = socket.gethostbyname(HOST)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except AttributeError:
            print 'Some systems do not support SO_REUSEPORT'
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)
        self.client.bind(('', PORT))
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(self.intf))
        self.client.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(IP) + socket.inet_aton(self.intf))

    def ack(self):
        self.acked = False
        while not self.acked:
            header = self.listen().next()
            if header.get('data') in ['ack']:
                self.header.update(header)
                self.acked = True
                print 'Header: ', self.header
            else:
                print 'Try again..'

    def listen(self):
        while True:
            msg, self.addr = self.client.recvfrom(self.buf_size)
            msg = jload(msg)
            if msg.get('data') in ['sig']:
                yield msg
            elif msg.get('data') in ['off']:
                yield msg
                break
            elif msg.get('data') in ['ack']:
                yield msg
                break

    def close(self):
        print socket.inet_aton(self.addr[0]) + socket.inet_aton('0.0.0.0')
        self.client.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP, socket.inet_aton(self.addr[0]) + socket.inet_aton('0.0.0.0'))
        self.client.close()

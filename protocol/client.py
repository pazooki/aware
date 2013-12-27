from definition import *


class Client(object):
    def __init__(self):
        self.buf_size = 1024
        self.acked = False
        self.addr = None
        self.header = HEADER
        self.intf = socket.gethostbyname(HOST)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)
        self.client.bind(('', PORT))
        self.client.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(self.intf))

    def ack(self):
        self.acked = False
        while not self.acked:
            signal = self.listen().next()
            if signal.get('data') in ['ack']:
                self.header.update(signal)
                self.acked = True
                print 'Header: ', self.header
            else:
                print '\rTry again..',

    def listen(self):
        while True:
            msg, self.addr = self.client.recvfrom(self.buf_size)
            msg = jload(msg)
            if msg.get('data') in ['sig']:
                yield msg
            elif msg.get('data') in ['ack']:
                yield msg
                break
            elif msg.get('data') in ['off']:
                break

    def close(self):
        print 'Closing time..'
        self.client.close()

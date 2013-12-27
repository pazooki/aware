from protocol.client import Client
from protocol.signal import Signal

if '__main__' == __name__:
    client = Client()
    client.ack()
    for data in client.listen():
        signal = Signal(data)
        print 'Index: %s  Channels: %s  Signals: %s' % (signal.index, signal.channels, signal.signals)
    client.close()


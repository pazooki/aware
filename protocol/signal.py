
class Signal(object):
    def __init__(self, signal):
        self.signals = signal.get('signals')
        self.index = signal.get('index')
        self.data = signal.get('data')
        self.latency = signal.get('latency')

    def channel(self, number):
        if number < self.channels:
            return self.signals[number]

    @property
    def channels(self):
        return len(self.signals)
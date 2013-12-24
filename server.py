import math
import itertools
import protocol


class Sine(object):
    """
    A sine wave oscillator.
    """
    
    sr = 44100
    ksmps = 5
    
    def __init__(self, amp=1.0, freq=440, phase=0.0):
        self.amp = amp
        self.freq = float(freq)
        self.phase = phase
        self.index = 0
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.index >= self.ksmps:
            raise StopIteration

        self.index += 1
        v = math.sin(self.phase * 2 * math.pi)
        self.phase += self.freq / self.sr
        return v * self.amp

if __name__ == "__main__":
    # protocol.server(i + j for i, j in itertools.izip(Sine(1, 4410, 0.25), Sine(0.5, 8820)))
    server = protocol.Server()
    server.listen()
    server.ack()
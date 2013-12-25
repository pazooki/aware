import math


# http://zacharydenton.com/generate-audio-with-python/

class Sine(object):
    """
    A sine wave oscillator.
    """

    sr = 44100
    ksmps = 10

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

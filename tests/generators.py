import math


# http://zacharydenton.com/generate-audio-with-python/

class Wave(object):
    """
    A sine wave oscillator.
    """

    def __init__(self, form='sin', amp=1.0, freq=440, phase=0.0, ksmps=10):
        self.amp = amp
        self.freq = float(freq)
        self.phase = phase
        self.index = 0
        self.sr = 44100
        self.ksmps = ksmps
        self.form = form
        self.waves = {'sin': math.sin, 'cos': math.cos}
        self.func = self.waves.get(self.form)

    def __iter__(self):
        return self

    def next(self):
        if self.index >= self.ksmps:
            raise StopIteration

        self.index += 1
        v = self.func(self.phase * 2 * math.pi)
        self.phase += self.freq / self.sr
        return v * self.amp

import itertools
from protocol.publisher import Publisher
from generators import Wave

if __name__ == "__main__":
    pub = Publisher()
    pub.open()
    pub.ack()
    for signals in itertools.izip(
            Wave(form='sin', amp=1, freq=1000, ksmps=300),
            Wave(form='cos', amp=5, freq=4400, ksmps=300),
            Wave(form='sin', amp=2, freq=1400, ksmps=300),
            Wave(form='cos', amp=1, freq=2400, ksmps=300),
            Wave(form='sin', amp=7, freq=6400, ksmps=300),
            Wave(form='sin', amp=3, freq=3400, ksmps=300),
            Wave(form='cos', amp=4, freq=2400, ksmps=300)
    ):
        pub.publish(signals)
    pub.close()

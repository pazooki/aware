import itertools
from protocol.publisher import Publisher
from generators import Wave

if __name__ == "__main__":
    server = Publisher()
    server.open()
    for sin, cos in itertools.izip(Wave(form='sin', amp=1, freq=1000, ksmps=100), Wave(form='cos', amp=5, freq=4400, ksmps=100)):
        server.transfer([sin, cos])
    server.close()
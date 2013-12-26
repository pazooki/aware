import itertools
from protocol.server import Server
from generators import Wave

if __name__ == "__main__":
    server = Server()
    server.ack()
    for sin, cos in itertools.izip(Wave(form='sin', amp=1, freq=1000), Wave(form='cos', amp=0.5, freq=440)):
        server.transfer('sig', [sin, cos])
    server.close()
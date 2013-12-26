import math
import itertools
from aware.protocol.server import Server
from generators import Sine

if __name__ == "__main__":
    # protocol.server(i + j for i, j in itertools.izip(Sine(1, 4410, 0.25), Sine(0.5, 8820)))
    server = Server()
    server.ack()
    for i in Sine(0.5, 8820):
        payload = [i]
        print payload
        server.transfer(payload)

    # for i, j in itertools.izip(Sine(1, 4410, 0.25), Sine(0.5, 8820)):
    #     payload = [i + j, i - j, i * j]
    #     print payload
    #     server.transfer(payload)
from protocol.subscriber import Subscriber

if '__main__' == __name__:
    client = Subscriber()
    client.listen()
    client.close()
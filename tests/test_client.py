from protocol.client import Client

if '__main__' == __name__:
    client = Client()
    client.ack()
    for msg in client.listen():
        print msg
    client.close()


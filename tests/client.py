from aware import protocol

if '__main__' == __name__:
    client = protocol.Client()
    client.ack()
    for msg in client.listen():
        print msg


import protocol


if '__main__' == __name__:
    client = protocol.Client()
    acked = False
    while not acked:
        acked = client.ack()

    while True:
        msg = client.receive().next()
        if msg:
            print '%s,%s,%s' % (msg.get('index'), msg.get('distance'), msg.get('signals'))
        else:
            break


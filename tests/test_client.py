from protocol.subscriber import Subscriber

if '__main__' == __name__:
    sub = Subscriber()
    sub.ack()
    for data in sub.listen():
        print data.get('signals')
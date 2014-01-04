from protocol.subscriber import Subscriber

if '__main__' == __name__:
    sub = Subscriber()
    for data in sub.listen():
        print data
    sub.close()
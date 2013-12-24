import protocol
import ujson


if '__main__' == __name__:
    client = protocol.Client(ujson.dumps(protocol.HEADER))
    client.ack()

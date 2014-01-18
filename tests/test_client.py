from protocol.subscriber import Subscriber
from libs.io.disk import matrix_to_csv
from libs.filters.extract import get_field, get_channels, get_channel
from libs.windows.queue import takesample, indexify
from libs.learn.transform import bandpass


if '__main__' == __name__:
    sub = Subscriber()
    sub.ack()
    signals = get_field(sub.listen(), 'signals')
    signals = matrix_to_csv('/var/log/test_1.csv', signals)
    original, samples = takesample(signals, 50)

    for sample in bandpass(get_channel(samples, 0)):
        print sample

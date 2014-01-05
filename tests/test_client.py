from protocol.subscriber import Subscriber
from libs.io.disk import matrix_to_csv
from libs.filters.extract import get_field, get_channels
from libs.windows.queue import takesample, indexify
from libs.visuals.plot import Animate


if '__main__' == __name__:
    sub = Subscriber()
    sub.ack()
    signals = get_field(sub.listen(), 'signals')
    # channel = matrix_to_csv('/var/log/test_1.csv', signals)
    original, samples = takesample(signals, 50)
    visual = Animate(signal for signal in indexify(get_channels(samples, [4])))
    print 'Visualizing...'
    visual.play()
    print 'Visualization is done.'
    for signal in original:
        print signal

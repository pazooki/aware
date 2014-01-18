

def get_field(input_iter, field):
    for data in input_iter:
        yield data.get(field, None)


def get_channels(input_iter, channels):
    for signals in input_iter:
        if len(signals) >= max(channels):
            yield [signals[channel] for channel in channels]


def get_channel(input_iter, channel):
    for signals in input_iter:
        if len(signals) >= channel:
            yield signals[channel]
import numpy


def apply_func(input_iter, sniff_func, *args):
    return sniff_func(input_iter, *args)


def takesample(input_iter, size):
    """
    keep the size small please.
    """
    samples = []
    while len(samples) < size:
        samples.append(input_iter.next())

    def original_iter():
        for sample in samples:
            yield sample
        for data in input_iter:
            yield data
    return original_iter(), samples


def nparray(input_list):
    return numpy.array(input_list)


def indexify(input_list):
    index = 0
    for data in input_list:
        yield index, data
        index += 1
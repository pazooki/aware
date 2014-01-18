import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq


def vectorize(input_iter):
    for ridx, row in enumerate(input_iter):
        for cidx, column in enumerate(row):
            yield ridx, cidx, column


def matrixify(input_iter):
    return np.matrix.matrix(input_iter, dtype=np.float64)


def biconvex(matrix):
    return np.std(matrix, dtype=np.float64)


def biconcave(matrix, target):
    dim = matrix.shape
    if dim > target:
        for i in xrange(target):
            matrix[dim[0]/i:]


def bandpass(input_iter):
    """
    filter extreme low and high only from a single channel
    """
    signal = np.array(list(input_iter))
    print signal.size
    time = np.linspace(0, 10, 20)
    w = fftfreq(signal.size, d=time[1] - time[0])
    f_signal = rfft(signal)
    cut_f_signal = f_signal.copy()
    cut_f_signal[(w < 6)] = 0
    cut_signal = irfft(cut_f_signal)
    print cut_signal.size
    return cut_signal


def sparse():
    """
    yield sparsed of a chunk
    """
    pass


def blockshaped(matrix, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = matrix.shape
    return matrix.reshape(h//nrows, nrows, -1, ncols).swapaxes(1,2).reshape(-1, nrows, ncols)
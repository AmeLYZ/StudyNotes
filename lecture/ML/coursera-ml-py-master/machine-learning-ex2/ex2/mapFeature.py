import numpy as np


def map_feature(x1, x2):
    # result  1  X1  X2  X1^2  X1X2  X2^2  X1^3  X1^2*X2  X1*X2^2  X2^3 ...
    degree = 6

    x1 = x1.reshape((x1.size, 1))
    x2 = x2.reshape((x2.size, 1))
    result = np.ones(x1[:, 0].shape)

    for i in range(1, degree + 1):
        for j in range(0, i + 1):
            result = np.c_[result, (x1**(i-j)) * (x2**j)]

    return result

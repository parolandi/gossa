
import numpy as np

def bilinear_linear(x):
    """
    Evaluates a bilinear and linear system according to
    [x1*x2, x1+x2]
    :param x: an array of size 2
    :return: an numpy array of size 2 with the function above evaluated
    """
    return np.asarray([x[0]*x[1], x[0]+x[1]])
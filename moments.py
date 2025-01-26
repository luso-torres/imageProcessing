import numpy as np

def second_order_moment(hist: np.ndarray) -> float:
    """
    Calculate the second-order moment of a histogram.
    """
    moment = 0
    for i in range(len(hist)):
        moment += i**2 * hist[i]
    return moment

import numpy as np

def third_order_moment(hist: np.ndarray) -> float:
    """
    Calculate the third-order moment of a histogram.
    """
    moment = 0
    for i in range(len(hist)):
        moment += i**3 * hist[i]
    return moment

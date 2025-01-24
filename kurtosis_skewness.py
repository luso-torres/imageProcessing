import numpy as np
import moments

def skewness(hist: np.ndarray, expectation: float) -> float:
    """
    Calculate the skewness of a histogram.
    """
    central_third_moment = moments.central_third_order_moment(hist, expectation)
    central_second_moment = moments.central_second_order_moment(hist, expectation)
    skewness = central_third_moment / (central_second_moment**(3/2))
    return skewness

import numpy as np

def kurtosis(hist: np.ndarray, expectation: float) -> float:
    """
    Calculate the kurtosis of a histogram.
    """
    central_fourth_moment = moments.central_fourth_order_moment(hist, expectation)
    central_second_moment = moments.central_second_order_moment(hist, expectation)
    kurtosis = central_fourth_moment / (central_second_moment**2)
    return kurtosis

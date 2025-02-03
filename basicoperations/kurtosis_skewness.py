import numpy as np
from . import moments

def skewness(scale: np.ndarray, pmf: np.ndarray, expectation: float) -> float:
    """
    Calculate the skewness of a pmf.
    """
    central_third_moment = moments.central_third_order_moment(scale,pmf, expectation)
    central_second_moment = moments.central_second_order_moment(scale,pmf, expectation)
    skewness = central_third_moment / (central_second_moment**(3/2))
    return skewness

import numpy as np

def kurtosis(scale: np.ndarray,pmf: np.ndarray, expectation: float) -> float:
    """
    Calculate the kurtosis of a random variable.
    """
    central_fourth_moment = moments.central_fourth_order_moment(scale,pmf, expectation)
    central_second_moment = moments.central_second_order_moment(scale,pmf, expectation)
    kurtosis = central_fourth_moment / (central_second_moment**2)
    return kurtosis

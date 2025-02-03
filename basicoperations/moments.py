import numpy as np

def second_order_moment(scale: np.ndarray, pmf: np.ndarray) -> float:
    """
    Calculate the second-order moment of a pmf.
    """
    scale = scale.astype(np.float64)
    moment_values = scale ** 2 * pmf
    moment = np.sum(moment_values)
    return moment

def third_order_moment(scale,pmf) -> float:
    """
    Calculate the third-order moment of a pmf.
    """
    scale = scale.astype(np.float64)
    moment =0
    for i in range(len(pmf)):
        moment += scale[i]**3 * pmf[i]
    return moment

def central_second_order_moment(scale: np.ndarray,pmf: np.ndarray, expectedValue: float) -> float:
    """
    Calculate the central second-order moment of a pmf.
    """
    scale = scale.astype(np.float64)
    moment = 0
    for i in range(len(pmf)):
        moment += (scale[i] - expectedValue)**2* pmf[i]
    return moment/len(pmf)

def central_third_order_moment(scale: np.ndarray, pmf: np.ndarray, expectedValue: float) -> float:
    """
    Calculate the central third-order moment of a pmf.
    """
    moment = 0
    scale = scale.astype(np.float64)
    for i in range(len(pmf)):
        moment += (scale[i] - expectedValue)**3*pmf[i]
    return moment

def central_fourth_order_moment(scale: np.ndarray, pmf: np.ndarray, expectedValue: float) -> float:
    """
    Calculate the central fourth-order moment of a pmf.
    """
    moment = 0
    scale = scale.astype(np.float64)
    for i in range(len(pmf)):
        moment += (scale[i]-expectedValue)**4* pmf[i]
    return moment

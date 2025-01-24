import numpy as np
def calculateValues(xpmf: np.array) -> float:
    """" ... """
    meanValue = np.mean(xpmf) #aritmetica
    expectedValue = np.sum(xpmf)
    modeValue = np.argmax(xpmf)
    medianValue = np.median(xpmf)
    return meanValue,expectedValue,modeValue,medianValue
import numpy as np
def calculateValues(pmf: np.array,xpmf: np.array) -> float:
    """" ... """
    meanValue = np.mean(pmf) #aritmetica
    expectedValue = np.sum(xpmf)

    modeValue = np.argmax(xpmf)
    medianValue = np.median(xpmf)
    return meanValue,expectedValue,modeValue,medianValue
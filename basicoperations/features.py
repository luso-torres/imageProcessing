import numpy as np
def calculateValues(uniqueValues: np.array, pmf: np.array,xpmf: np.array) -> int:
    """" ... """
    meanValue = np.mean(uniqueValues) #aritmetica
    expectedValue = np.sum(xpmf)
    modeValue = uniqueValues[np.argmax(pmf)]
    cdf = np.cumsum(pmf)
    medianValue =  uniqueValues[np.searchsorted(cdf, 0.5)]
    
    return meanValue,expectedValue,modeValue,medianValue
import numpy as np

def evaluateEntropy(pmf) -> float:
    entropy =0
    for p in range(len(pmf)):
        if pmf[p] > 0 :
            entropy += pmf[p] * np.log2(pmf[p] + 1e-20)
    return -entropy
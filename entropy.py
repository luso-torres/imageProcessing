import numpy as np

def evaluateEntropy(pmf) -> float:
    entropy =0
    for p in range(len(pmf)):
        entropy += p *pmf* np.log2(pmf[p]) 

    return -entropy 
import numpy as np

def evaluateEntropy(pmf) -> float:
    entropy =1
    for p in range(len(pmf)):
        if p == 0 :
            p =1
        entropy += p *pmf* np.log2(pmf[p]+ 1e-20) 

    return -entropy 
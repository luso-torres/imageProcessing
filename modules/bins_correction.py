#Function created to correct the bins

def binsCorrection(num_levels,unique,countsv):
    """
    Bins correction (inserting the zero states)
    Entries: quantization, distinct values of your image and the respective counter of your function
    """    
    unique_values = [0]*(int((num_levels)))
    counts = [0.0]*(int((num_levels)))
    for i in range(len(unique)):
    #print(unique[i])
        for j in range(num_levels):  
            if (unique[i] == 256/num_levels*j):
                unique_values[j] = unique[i]
                counts[j] = countsv[i]
                #print(counts[j])
    pmf = counts/(sum(counts))

    return pmf, unique_values,counts
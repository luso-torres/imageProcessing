import numpy as np
import sys
import os
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ..basicoperations import entropy, features, kurtosis_skewness, moments, requantize

def featureExtraction(image_array: str, fileNumber):
    a = 10
    # Requantize to 4 bits = 16 levels (e.g., 0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240 )
    # Requantize to 2 bits = 4 levels (e.g., 0, 64, 128, 192)
    # Requantize to 1 bit = 2 levels (e.g. 0, 256)
    num_levels = 2
    requantized_image = requantize.requantize_image(image_array, num_levels)
#Construct histogram
    unique_values, counts = np.unique(requantized_image, return_counts=True)
    pmf = counts/(sum(counts))
    xpmf = unique_values*pmf

# Calculating metrics
    meanValue,expectedValue, modeValue, medianValue = features.calculateValues(unique_values,pmf,xpmf)
#modeValue = unique_values[int(modePosition)-1]
#medianValue = unique_values[int(medianPosition)-1]

    secondOrderMoment = moments.second_order_moment(unique_values,pmf)
    thirdOrderMoment = moments.third_order_moment(unique_values,pmf)
    centralSecond = moments.central_second_order_moment(unique_values,pmf,expectedValue)
    centralThird = moments.central_third_order_moment(unique_values,pmf,expectedValue)
    skew = kurtosis_skewness.skewness(unique_values,pmf,meanValue)
    kurt = kurtosis_skewness.kurtosis(unique_values,pmf,meanValue)
    E = entropy.evaluateEntropy(pmf) 



    print("Media:", meanValue,"\nExpectancia:",expectedValue,"\nModa:",modeValue,"\nMediana:",medianValue)
    print(f'Momento 2: {secondOrderMoment},\n Segundo Central: {centralSecond}\nMomento 3: {thirdOrderMoment},\nTerceiro Central: {centralThird},\nSkewness: {skew},\nKurtosis: {kurt}')
    data = [counts, fileNumber]
    data = np.array(data)
    return data
import numpy as np
from PIL import Image
import requantize,plot,metrics, kurtosis_skewness, moments, entropy

# Load a grayscale image
# image = Image.open("D:/Documents and Education/Dropbox/Education/ESTOCASTICOS - 2 - 2024/trabalhos computacionais/Luso/5.png").convert("L")  # Convert to grayscale
# image = Image.open("D:/Documents and Education/Dropbox/Education/ESTOCASTICOS - 2 - 2024/trabalhos computacionais/Luso/Snap-310.jpg").convert("L") 
image = Image.open("D:/Documents and Education/Dropbox/Education/ESTOCASTICOS - 2 - 2024/trabalhos computacionais/Luso/CDR05_0017.jpg").convert("L")
# 5.png
# CDR05_0017.jpg
# Snap-310.jpg
# WP_20160127_088.jpg
# y87.jpg

# Convert image to a NumPy array
image_array = np.array(image)


# Requantize to 4 bits = 16 levels (e.g., 0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240 )
# Requantize to 2 bits = 4 levels (e.g., 0, 64, 128, 192)
# Requantize to 1 bit = 2 levels (e.g. 0, 256)
num_levels = 16
requantized_image = requantize.requantize_image(image_array, num_levels)

# Construct histogram
unique_values, counts = np.unique(requantized_image, return_counts=True)
pmf = counts/(sum(counts))
xpmf = unique_values*pmf

# Calculating metrics
meanValue,expectedValue, modeValue, medianValue = metrics.calculateValues(xpmf) #aritmetica
secondOrderMoment = moments.second_order_moment(xpmf)
thirdOrderMoment = moments.third_order_moment(xpmf)
skew = kurtosis_skewness.skewness(xpmf)
kurt = kurtosis_skewness.kurtosis(xpmf)
E = entropy.evaluateEntropy(xpmf) 
print("Media:", meanValue,"\nExpectancia:",expectedValue,"\nModa:",modeValue,"\nMediana:",medianValue)
print("Momento 2: ",secondOrderMoment,"\nMomento 3: ",thirdOrderMoment,"\nSkewness: ", skew,"\nKurtosis", kurt)
# Plot the histogram
plot.plots(unique_values,counts)

import numpy as np
from PIL import Image
import os

#import basicoperations
from basicoperations import *
from basicoperations import requantize

# Loadig a grayscale image

subfolder = "images"
folder_path = os.getcwd()
# Construct the full path
subfolder_path = os.path.join(folder_path, subfolder)

print('Address ',subfolder_path)

#auxiliary variables to select the image
choose = 1
i=1

for fileName in os.listdir(subfolder_path):
    if  (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')) and (not fileName.startswith('resized')):
        if (i==choose):
            print(f'Selected Image: {fileName}')
            image_path = os.path.join(subfolder_path, fileName)
            image = Image.open(image_path)
            image = image.convert("L")
            break
    i+=1

# Convert image to a NumPy array
image_array = np.array(image)


# Requantize to 4 bits = 16 levels (e.g., 0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240 )
# Requantize to 2 bits = 4 levels (e.g., 0, 64, 128, 192)
# Requantize to 1 bit = 2 levels (e.g. 0, 256)
num_levels = 8
requantized_image = requantize.requantize_image(image_array, num_levels)

# Construct histogram
unique_values, counts = np.unique(requantized_image, return_counts=True)
pmf = counts/(sum(counts))
xpmf = unique_values*pmf

# Calculating metrics
meanValue,expectedValue, modeValue, medianValue = features.calculateValues(unique_values,pmf,xpmf)


secondOrderMoment = moments.second_order_moment(unique_values,pmf)
thirdOrderMoment = moments.third_order_moment(unique_values,pmf)
centralSecond = moments.central_second_order_moment(unique_values,pmf,expectedValue)
centralThird = moments.central_third_order_moment(unique_values,pmf,expectedValue)
skew = kurtosis_skewness.skewness(unique_values,pmf,meanValue)
kurt = kurtosis_skewness.kurtosis(unique_values,pmf,meanValue)
E = entropy.evaluateEntropy(pmf) 



print("Media:", meanValue,"\nExpectancia:",expectedValue,"\nModa:",modeValue,"\nMediana:",medianValue)
print(f'Momento 2: {secondOrderMoment},\n Segundo Central: {centralSecond}\nMomento 3: {thirdOrderMoment},\nTerceiro Central: {centralThird},\nSkewness: {skew},\nKurtosis: {kurt}')

# Plot the histogram
plot.plots(unique_values,counts)

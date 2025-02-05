import numpy as np
from PIL import Image
import os
from pathlib import Path

#import basicoperations
from basicoperations import *
from basicoperations import requantize

# Loadig a grayscale image

subfolder = "Image dataset/Skin_Cancer"
cwd = Path.cwd()
data_file = cwd / "Data.csv"
folder_path = os.getcwd()
# Construct the full path
subfolder_path = os.path.join(folder_path, subfolder)

print('Address ',subfolder_path)

#auxiliary variables to select the image
choose = 1
i=1

#Selects the test file
for fileName in os.listdir(subfolder_path):
    if  (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')) and (not fileName.startswith('resized')):
        if (fileName.__contains__('36.jpg')):
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

unique, countsv = np.unique(requantized_image, return_counts=True)

# Bins correction (inserting the zero states)
unique_values = [0]*(int((num_levels)))
counts = [0.0]*(int((num_levels)))
for i in range(len(unique)):
    #print(unique[i])
    for j in range(num_levels):  
        if (unique[i] == 256/num_levels*j):
            unique_values[j] = unique[i]
            counts[j] = countsv[i]
            print(counts[j])
pmf = counts/(sum(counts))


# Calculating metrics
meanValue,expectedValue, modeValue, medianValue = features.calculateValues(unique_values,pmf,unique_values*pmf)


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

from modules import rewrite_files
rewrite_files.rewriteFiles(data_file)     
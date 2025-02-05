import numpy as np
from PIL import Image
import os
from pathlib import Path

#import basicoperations
#from basicoperations import *
from basicoperations import requantize
from modules.verify_file import verifyFile
from modules.bins_correction import binsCorrection
from modules import rewrite_files  
#from basicoperations import squared_range
from basicoperations import * 
from modules import initialization

# Loadig a grayscale image
#auxiliary variables to select the image
choose = 2
i=1

#from pathlib import Path
cwd = Path.cwd()
target_dir = cwd / "Image dataset"
data_file = cwd / "Data_statistics.csv"
first_line = "h[0],h[1],h[2],h[3],h[4],h[5],h[6],h[7], ID"
initialization.initialize(first_line,data_file)


for fileName in (target_dir.rglob("*")):
    fileName = str(fileName)
    if  (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')): #and (fileName.__contains__("WP_20150917_008")):
        #if (i==choose):
        #print(f'Selected Image: {fileName}')
        #image_path = os.path.join(subfolder_path, fileName)
        image = Image.open(fileName)
        image = image.convert("L")
        image_array = np.array(image)
        num_levels = 8
        requantized_image = requantize.requantize_image(image_array, num_levels)
        
        unique_values, counts = np.unique(requantized_image, return_counts=True)
        
        pmf, unique_values, counts = binsCorrection(num_levels,unique_values,counts)        

# Construct histogram
        xpmf = unique_values*pmf
        
        
# Feature calculation
        meanValue,expectedValue, modeValue, medianValue = features.calculateValues(unique_values,pmf,unique_values*pmf)
        secondOrderMoment = moments.second_order_moment(unique_values,pmf)
        thirdOrderMoment = moments.third_order_moment(unique_values,pmf)
        centralSecond = moments.central_second_order_moment(unique_values,pmf,expectedValue)
        centralThird = moments.central_third_order_moment(unique_values,pmf,expectedValue)
        skew = kurtosis_skewness.skewness(unique_values,pmf,meanValue)
        kurt = kurtosis_skewness.kurtosis(unique_values,pmf,meanValue)
        Ent = entropy.evaluateEntropy(pmf) 

        data = [0]*8
        data[0] = expectedValue
        data[1] = modeValue
        data[2] = medianValue
        data[3] = squared_range.squaredRange(unique_values)
        data[4] = centralSecond
        data[5] = skew
        data[6] = kurt
        data[7] = Ent
        #data[6] = kurt
        
        #data[7] = kurt
        


        if fileName.__contains__('Alzheimer'):
            number =0
        elif fileName.__contains__('COVID'):
            number =1
        elif fileName.__contains__('Brazilian_Seeds'):
            number =2
        elif fileName.__contains__('Brazilian_Leaves'):
            number =3
        else:
            number =4
#write the files
        verifyFile(data, number,data_file)
#rewrite the original
#rewrite_files.rewriteFiles(data_file)      
data_sorted_file = 'Data_statistics_sorted.csv'
initialization.initialize(first_line,data_sorted_file)
rewrite_files.rewriteFiles(data_file,data_sorted_file) 
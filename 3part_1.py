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
from modules import initialization

# Loadig a grayscale image
#auxiliary variables to select the image
choose = 2
i=1

#from pathlib import Path
cwd = Path.cwd()
data_file = cwd / "Data.csv"
target_dir = cwd / "Image dataset"
first_line = "h[0],h[1],h[2],h[3],h[4],h[5],h[6],h[7], ID"
initialization.initialize(first_line,data_file)
        
for fileName in (target_dir.rglob("*")):
    fileName = str(fileName)
    if  (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')): #and (fileName.__contains__("WP_20150917_008")):
        #if (i==choose):
        print(f'Selected Image: {fileName}')
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
        verifyFile(pmf, number,data_file)
#rewrite the original
    else:
        continue
data_sorted_file = 'Data_sorted.csv'
initialization.initialize(first_line,data_sorted_file)
rewrite_files.rewriteFiles(data_file,data_sorted_file)      
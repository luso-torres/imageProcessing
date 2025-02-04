import os
import numpy as np
from pathlib import Path

#from ..basicoperations import entropy, features, kurtosis_skewness, moments, requantize
#import feature_extraction, image_extraction, save_file, verify_file

subfolder = "images"
folder_path = os.getcwd()
#print(folder_path)
folder_path = Path(__file__)
parent_path = folder_path.parent
print(parent_path)
# Construct the full path
#subfolder_path = os.path.join(parent_path, subfolder)
subfolder_path = parent_path
print('Address ',subfolder_path)

i= len(os.listdir(subfolder_path))
data = []
# for fileName in i:
#     np.append(data,image_extraction.imageExtraction(fileName))

# print(data.reshape(8,i))
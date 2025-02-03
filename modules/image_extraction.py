import numpy as np
import os
from PIL import Image

def imageExtraction(choose: int):
    subfolder = "images"
    folder_path = os.getcwd()
# Construct the full path
    subfolder_path = os.path.join(folder_path, subfolder)

    print('Address ',subfolder_path)

#auxiliary variables to select the image
    
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
    return image_array
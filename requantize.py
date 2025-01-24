import numpy as np
def requantize_image(image, num_levels):
    """" Function to requantize the image"""
    max_value = 255  # Maximum grayscale intensity
    step = (max_value+1) / num_levels  # Size of each interval
    quantized_image = (image // step) * step  # Map to nearest interval
    return quantized_image.astype(np.uint8)

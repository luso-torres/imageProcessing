# Image Processing for Stochastic Class Discrimination

Classifier algorithm for images with accuracy evaluation. Class discrimination utilizes Naïve Bayes, Linear, and
Quadratic discriminators. Currently in development.

## 1. Image Analysis

The first section of this project is designed to import and manipulate images of any format. More specifically, the set of images below were used as references for the algorithm.


<div align="center">
  <table>
    <tr>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_5.png" alt="Description" width="300">
        <p><i>Breast X-ray</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_CDR05_0017.jpg" alt="Description" width="300">
        <p><i>Brain X-ray</i></p>
      </td>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_Snap-310.jpg" alt="Description" width="300">
        <p><i>Nut</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_WP_20160127_088.jpg" alt="Description" width="300">
        <p><i>Leaf</i></p>
      </td>
       <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/Image%20dataset/Skin_Cancer/1.jpg" alt="Description" width="300">
        <p><i>Skin Cancer</i></p>
      </td>
    </tr>
  </table>
</div>

## 2. Grayscale

As described above, now, we implement the codes

``` python
import PIL as Image
folder_path = os.getcwd()
    for fileName in os.listdir(folder_path):
        if (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')):
                image = Image.open(f'.\images\{fileName}').convert("L")
```

Responsible for reading the images and converting them in a grayscale equivalent image. The library Image (PIL), has the function open that allow us to analyze our dataset;


## 3. Generating the Histograms

The following histograms were obtained by the logic:
``` python
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
pmf = [0]*int(num_levels)
for i in range(num_levels):
    pmf[i] = round(counts[i]/float((sum(counts))),4)
```

Then by applying the `matplotlib` library with 8 bins (8 bits quantization of the original image):
<div align="center">
  <table>
    <tr>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/covid_pmf.png" alt="Description" width="300">
        <p><i>Breast X-ray</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/alzheimer_pmf.png" alt="Description" width="300">
        <p><i>Brain X-ray</i></p>
      </td>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/seed_pmf.png" alt="Description" width="300">
        <p><i>Nut</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/leaf_pmf.png" alt="Description" width="300">
        <p><i>Leaf</i></p>
      </td>
       <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/cancer_pmf.png" alt="Description" width="300">
        <p><i>Skin Cancer</i></p>
      </td>
    </tr>
  </table>
</div>

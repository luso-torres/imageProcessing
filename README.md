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
        <p><i>Brain with pathology</i></p>
      </td>
    </tr>
  </table>
</div>

## 2. Grayscale

As described above, now, we implement the codes

``` python
folder_path = os.getcwd()
    for fileName in os.listdir(folder_path):
        if (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')):
                image = Image.open(f'.\images\{fileName}').convert("L")
```

Responsible for reading the images and converting them in a grayscale equivalent image.

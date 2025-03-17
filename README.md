# Image Classifier applying Stochastic Class Discrimination

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

# Generating Features
For this project the following features will be considered:
Mean, representing the central value of our dataset, expressed in terms of: 

$$\bar{X} = \frac{1}{N}\sum_{x=0}^{N-1} P_X (x)$$

where 
- $X$ is a random variable.
- $N$ is the total number of samples.
- $P_X$ is the probability mass function of the random variable X.
- $x$ is the $i$-th random variable of the sum operation.

The expectation operator, representing a long-term average we would expect if you repeated it infinitely under the same conditions:

$$\mathbb{E}[X] = \mu_X = \sum_{x=0}^{N-1} xP_X(x) $$

where
- $\mu_X$ is the true average of our sample space.
- $X$ is a random variable
- $N$ is the total number of samples
- $P_X$ is the probability mass function of the random variable X

The mode, which represents the value with most frequency, obtained for example with:
```python
def mode(num_levels,pmf) -> int:
    maxV = -np.inf # initialize
    for i in range (num_levels):
        if (pmf[i] >= maxV):
            position = i
            maxV = pmf[i]
    return position
```

The median, which divides the data in two equal sizes of 50%, obtained in terms of the Cumulative Distribution Function (CDF):
```python
def median(num_levels,pmf) -> int:
    cdf = [0]*num_levels #initialize
    cdf[0] = pmf[0]
    for i in range (1,num_levels):
        cdf[i] = pmf+cdf[i-1]
        if (cdf[i] >= 0.50):
            return i
\end{python}
```

Variance, also known as second order central moment of our data, reflecting the dispersion or degree of spreadness of the dataset. It shows how much individual values deviate from the mean. It can be obtained by:

$$Var(X) = E[(X-\mu_X)^2] = \sum_{x=0}^{N-1} x^2P_X(x)$$

_Skewness_, characterizing the imbalance or asymmetry of data around its mean:

$$\bar{\mu}_3= \mathbb{E}\left[ \left(\frac{X-\mu_X}{\sigma_X}\right)^3 \right]  = \frac{\mu_3}{\sigma_x^3}$$

_Kurtosis_, characterizing the peakedness or shape of data distribution tails. Higher peakedness suggests sharper peaks, whereas lower _kurtosis_ indicates flatter peaks. The mathematical representation is:

$$kurt[X]= \frac{\mu_4}{\sigma_4}=\left[\frac{\mathbb{E}\left[(X-\mu_X)^4\right]}{\left( \mathbb{E}[(X - \mu_X)^2]\right)^2}\right]$$


# Classification

# Model Evaluation and Cross Validation

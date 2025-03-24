# Image Classifier applying Stochastic Class Discrimination

Classifier algorithm for images with accuracy evaluation. Class discrimination utilizes Naïve Bayes, Linear, and
Quadratic discriminators. Updates in progress.

## 1. Image Analysis

The first section of this project is designed to import and manipulate images of any format. More specifically, the set of images below were used as references for the algorithm.


<div align="center">
  <table>
    <tr>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_5.png" alt="Description" width="300">
        <p><i>COVID</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_CDR05_0017.jpg" alt="Description" width="300">
        <p><i>Alzheimer</i></p>
      </td>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_Snap-310.jpg" alt="Description" width="300">
        <p><i>SEED</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/resized-images/resized_WP_20160127_088.jpg" alt="Description" width="300">
        <p><i>LEAF</i></p>
      </td>
       <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/Image%20dataset/Skin_Cancer/1.jpg" alt="Description" width="300">
        <p><i>SKIN CANCER</i></p>
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

The following histograms were obtained by the labels `unique_values` and `counts`, the first one identifying the quantization of the original image (0 to 256) according to the bin informed `num_levels`,(i.e. for 8 bins: 0, 32, 64, 96, 128, 160, 192, 224) and `counts` representing the frequency of each bin. 
<details><summary> Click here to see the code </summary> 

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
</details>
Then by applying the `matplotlib` library with 8 bins (8 bits quantization of the original image):
<div align="center">
  <table>
    <tr>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/covid_pmf.png" alt="Description" width="300">
        <p><i>COVID</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/alzheimer_pmf.png" alt="Description" width="300">
        <p><i>ALZHEIMER</i></p>
      </td>
      <td align="center">
       <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/seed_pmf.png" alt="Description" width="300">
        <p><i>SEED</i></p>
      </td>
      <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/leaf_pmf.png" alt="Description" width="300">
        <p><i>LEAF</i></p>
      </td>
       <td align="center">
        <img src="https://github.com/luso-torres/imageProcessing/blob/main/pmfs/cancer_pmf.png" alt="Description" width="300">
        <p><i>SKIN CANCER</i></p>
      </td>
    </tr>
  </table>
</div>

# Generating Features
For this project the following features will be considered: Mean, Expected Value, Mode, Median, Variance, Skewness, Kurtosis and Shannon's Entropy.

<details><summary> Click here to see an explanation of each feature
</summary>
  
## Mean $\mu$
Represents the central value of our dataset, expressed in terms of: 

$$\bar{X} = \frac{1}{N}\sum_{x=0}^{N-1} P_X (x)$$

where 
- $X$ is a random variable.
- $N$ is the total number of samples.
- $P_X$ is the probability mass function of the random variable X.
- $x$ is the $i$-th random variable of the sum operation.

## Expectation operator $\mathbb{E}[X]$
Represents a long-term average we would expect if you repeated it infinitely under the same conditions:

$$\mathbb{E}[X] = \mu_X = \sum_{x=0}^{N-1} xP_X(x) $$

where
- $\mu_X$ is the true average of our sample space.
- $X$ is a random variable
- $N$ is the total number of samples
- $P_X$ is the probability mass function of the random variable X

## Mode 
Represents the value with most frequency, obtained for example with:
```python
def mode(num_levels,pmf) -> int:
    maxV = -np.inf # initialize
    for i in range (num_levels):
        if (pmf[i] >= maxV):
            position = i
            maxV = pmf[i]
    return position
```

## Median
Divides the data in two equal sizes of 50%, obtained in terms of the Cumulative Distribution Function (CDF):
```python
def median(num_levels,pmf) -> int:
    cdf = [0]*num_levels #initialize
    cdf[0] = pmf[0]
    for i in range (1,num_levels):
        cdf[i] = pmf+cdf[i-1]
        if (cdf[i] >= 0.50):
            return i
```

## Variance
Also known as second order central moment of our data, reflects the dispersion or degree of spreadness of the dataset. It shows how much individual values deviate from the mean. It can be obtained by:

$$Var(X) = \sigma^2 = E[(X-\mu_X)^2] = \sum_{x=0}^{N-1} x^2P_X(x)$$

where
- $\sigma$ represents the standard deviation.
- $\sigma^2$ the variance (squared value of the standard deviation).
- 
## _Skewness_
characterizes the imbalance or asymmetry of data around its mean:

$$\bar{\mu}_3= \mathbb{E}\left[ \left(\frac{X-\mu_X}{\sigma_X}\right)^3 \right]  = \frac{\mu_3}{\sigma_x^3}$$

## _Kurtosis_
Characterizes the peakedness or shape of data distribution tails. Higher peakedness suggests sharper peaks, whereas lower _kurtosis_ indicates flatter peaks. The mathematical representation is:

$$kurt[X]= \frac{\mu_4}{\sigma_4}=\left[\frac{\mathbb{E}\left[(X-\mu_X)^4\right]}{\left( \mathbb{E}[(X - \mu_X)^2]\right)^2}\right]$$

Both _skewness_ and _kurtosis_ are given in terms of the third and fourth-order central moments, as we can observe by their definitions.

## Shannon's Entropy $\mathcal{H}$
Finally, the last feature is given in terms of the Shannon's Entropy, expressing the minimal number of bits necessary to represent a quantized image:

$$\mathcal{H} = - \sum_{x=0}^{N-1} P_X(x) log_2 [P_X(x)]$$


  
</details>
By applying each definition, the resulting features for the five figures are resumed in the table bellow:

| **Feature**           | COVID  | Alzheimer | Seed  | Leaf  | Cancer |
|------------------------|--------|-----------|-------|-------|--------|
| Mean                  | 112    | 112       | 144   | 128   | 112    |
| Expectation           | 103.18 | 65.71     | 194.37| 121.16| 156.07 |
| Mode                  | 0      | 0         | 224   | 96    | 160    |
| Median                | 96     | 0         | 224   | 128   | 160    |
| Variance              | 681.74 | 859.13    | 445.89| 223.69| 122.61 |
| 3rd Central Moment    | -5.66×10<sup>4</sup> | 4.37×10<sup>5</sup> | -3.37×10<sup>5</sup> | 2.07×10<sup>4</sup> | -5.07×10<sup>4</sup> |
| **Skewness**          | -11.09 | -16.29    | 24.07 | 19.71 | 23.56  |
| **Kurtosis**          | 112.87 | 81.93     | 76.11 | 156.20| 103.81 |
| 2nd Moment            | 1.61×10<sup>4</sup> | 1.12×10<sup>4</sup> | 4.13×10<sup>4</sup> | 1.65×10<sup>4</sup> | 2.53×10<sup>4</sup> |
| 3rd Moment            | 2.73×10<sup>6</sup> | 2.08×10<sup>6</sup> | 9.09×10<sup>6</sup> | 2.45×10<sup>6</sup> | 4.21×10<sup>6</sup> |
| Entropy               | 2.81   | 2.26      | 1.01  | 2.36  | 1.79   |


# 4. Generating a CSV with the Database

To generate a csv with our database, we run our algorithm for each image and then save it in a line inside this file.
```python
cwd = Path.cwd()
target_dir = cwd / "Image dataset"
for fileName in (target_dir.rglob("*")):
    fileName = str(fileName)
    if  (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')):
        print(f'Selected Image: {fileName}')
        image = Image.open(fileName)
```

For saving the histogram of each image or choosing the statistical values, consider the following program:
```python
data = [0]*8 #prior generation of each cell
data[0] = expectedValue
data[1] = modeValue
data[2] = medianValue
data[3] = squared_range.squaredRange(unique_values)
data[4] = centralSecond
data[5] = skew
data[6] = kurt
data[7] = Ent

## For saving the histogram
# data = pmf

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
```

To save the values of each image as a row, two functions were elaborated: `initialization.py`, which creates the csv file in the directory and `verify_file.py` that saves each row containing the features.

<details>
<summary>Click here to see the full description of the functions</summary>

```python
import os
def initialize(line_to_append,file_name):
    print("File initialized")
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()  # Read the content of the file

        if content.__contains__(line_to_append):
            print(f"Line already exists in {file_name}")
            return  # Exit if the line already exists
    else:
        # If the file doesn't exist, it will be created when we append
        print(f"{file_name} does not exist. It will be created.")
        with open(file_name,"a") as file:
            file.write(line_to_append+'\n')

    return
```

  
  ```python
import os
import numpy as np
def verifyFile(line,number,file_name) -> None:
    line_to_append = f'{line},{number}'

# Read the content of the file if it exists
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()  # Read the content of the file

        if line_to_append in content:
            print(f"Line already exists in {file_name}")
            return  # Exit if the line already exists
    else:
# If the file doesn't exist, it will be created when we append
        print(f"{file_name} does not exist. It will be created.")

# Append the line to the file if it's not already in the content
    with open(file_name, "a") as file:
        file.write(",".join(map(str, line)) + f',{number}\n')  # Write the new line to the file
        print(f"Line appended to {file_name}")
    return None
```
</details>

# 5. Classification
As previously discussed, the chosen classifiers for this task are Gaussian Naïve Bayes, Linear Discriminant Analysis (LDA), and Quadratic Discriminant Analysis (QDA).

<details><summary> Click here to check a brief overview</summary>

## Linear Discriminant Analysis (LDA)
Linear Discriminant Analysis (LDA) is a probabilistic classifier that identifies a projection maximizing the separation between class means while minimizing variance within each class. LDA operates under the following assumptions:

- Each class follows a multivariate Gaussian distribution.
- All classes share a common covariance matrix.
- The decision boundary is linear.

LDA relies on the estimated mean vector ($\mu$) and covariance matrix ($\Sigma$) for each class to compute the discriminant function:

$$g_i(x) = x^T\Sigma^{-1}\mu_i - \frac{1}{2} \mu_i^T\Sigma^{-1}\mu_i + \ln P(y=i) $$

Where:

- $P(y=i)$ denotes the prior probability of class $i$.
- $g_i(x)$ represents the discriminant score, which indicates the similarity of the observation $x$ to class $i$.

## Quadratic Discriminant Analysis (QDA)
Quadratic Discriminant Analysis (QDA) extends LDA by relaxing the assumption of a shared covariance matrix. This allows each class to have its unique covariance matrix ($\Sigma_i$), resulting in a quadratic decision boundary.

Like LDA, QDA begins by estimating the mean vector ($\mu_i$) and covariance matrix ($\Sigma_i$) for each class. The discriminant function for QDA is given by:

$$g_i(x) = -\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i) - \frac{1}{2} \ln |\Sigma_i| + \ln P(y=i) $$

With its curved decision boundary, QDA offers greater flexibility compared to LDA. However, this increased flexibility comes at the cost of requiring a larger training dataset.

## Gaussian Naïve Bayes
Its a probabilistic classifier based on the Bayes Theorem:

$$P(y|X) = \frac{P(X|y)P(y)}{P(X)}$$

Where:
- $P(y|X)$ is the _a posteriori_ probability (the probability of class y given X). This probability is also known as the similarity (how well X fits y).
- $P(y)$ refers to the current knowledge or assumptions of a parameter before observing new data, or simply _prior_.
- $P(X)$ refers to the evidence, new data or information utilized to modify your prior premisses (constant between all classes).

One of the main attributes of the technique is the independence of each feature, i.e., the GNB Classifier assumes that $x_1,x_2,...,x_d$ are conditionally independent for a given class y:

$$P(X|y) = P(x_1|y)P(x_2|y)...P(x_d|y)$$

The classifier operation is given by the value of the prior of each class $P(y)$, estimation of the feature distribution $P(x_j|y)$ for each feature $x_j$ and finally, the Bayes Theorem application for classification of new points.

With respect to the types of Naïve Bayes classifiers, we have:
1. Gaussian Naïve Bayes: Assume that the features follows a normal distribution.
2. Multinomial Naïve Bayes: Utilized for cases where the features are counts or data frequencies, i.e., how much times a word appears in a document.
3. Bernoulli Naïve Bayes: Operates with binary data.
</details>


## Implementation:

The implementation is based on the use of the `sklearn` along with the `pandas` framework with the following functions `model_selection.train_test_split` for the separation of the samples for test and train. The classifiers are implemented with the libraries `discriminant_analysis` and `naive_bayes`:
```python
import  numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB

# 1. Loading data.csv
data = pd.read_csv('feature_dataset.csv')

# We suppose that the last column is the class
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Dividing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
```

And classifiers:
```python
# a) Bayes Law (Gaussian Naive Bayes)
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)
nb_predictions = nb_classifier.predict(X_test)

# b) Linear discriminator
lda_classifier = LinearDiscriminantAnalysis(solver='eigen', shrinkage='auto')
lda_classifier.fit(X_train, y_train)
lda_predictions = lda_classifier.predict(X_test)

# c) Quadratic Discriminator
qda_classifier = QuadraticDiscriminantAnalysis(reg_param=0.1)
qda_classifier.fit(X_train_scaled, y_train)
qda_predictions = qda_classifier.predict(X_test_scaled)
```
# 6. Model Evaluation and Cross Validation
The metrics for measuring the effectiveness of the classifiers are derived from the Confusion Matrix, where _precision_, _recall_, _F1-Score_ and _Support_ were considered. In terms of the confusion matrix for a binary case, four elements are considered:
- True Positives (TP);
- False Positives (FP);
- False Negatives (FN); and
- True Negatives (TN)
arranged as following:



## Implementation
`metrics.classification_report` and `metrics.confusion_matrix`

import tensorflow.keras as tf
import matplotlib.pyplot as plt
import numpy as npimport tensorflow.keras as tf
import matplotlib.pyplot as plt
import numpy as np

### Import the dataset
mnist = tf.datasets.mnist
(xtrain,ytrain),(xtest,ytest) = mnist.load_data()

xtrain.shape

ytrain.shape
plt.imshow(xtrain[100],cmap='gray')
ytrain[100]

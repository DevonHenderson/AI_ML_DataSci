from sklearn.datasets import load_iris

iris = load_iris()
print("Looking at IRIS dataset")
print("Keys: ", iris.keys())

n_samples, n_features = iris.data.shape
print("Samples: ", n_samples,"\nFeatures: ", n_features)
print("First Instance of data: ", iris.data[0])
print("Second Instance of data: ", iris.data[1])
print("Last instance of data: ", iris.data[n_samples-1])

print("Iris Target Shape: ", iris.target.shape)
print("Iris X 1st Instance: ", iris.data[0])
print("Iris y 1st instance target: ", iris.target[0])

print("Iris Target names: ", iris.target_names)
print("Entire target/label vector y", iris.target)

####

import numpy as np
import matplotlib.pyplot as plt

def plot_iris_projection(x_index, y_index):
    #Label with correct target names
    formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])
    #Create plot
    plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
    plt.colorbar(ticks=[0,1,2], format=formatter)
    plt.xlabel(iris.feature_names[x_index])
    plt.ylabel(iris.feature_names[y_index])
    
x_index=3 #Petal width 
y_index=2 #Petal Length
plot_iris_projection(x_index, y_index)

######

from sklearn.datasets import get_data_home
print("\nFetch datasets home: ", get_data_home()) #data downloaded using the fetch_ scripts 

####

from sklearn.datasets import load_digits
digits = load_digits()
print("Digits Keys: ", digits.keys())
n_samples, n_features = digits.data.shape
print("Samples: ", n_samples,"\nFeatures: ", n_features)

print("Digits 1st instance data (X): ", digits.data[0])
print("Digits Targets (y): ", digits.target)
print("Data Shape: ", digits.data.shape)
print("Image Shape: ", digits.images.shape)

########

import pylab as plot
fig = plot.figure(figsize=(3, 3))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(digits.data.shape[1]):
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plot.cm.binary, interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]))

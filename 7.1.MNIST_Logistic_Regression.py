# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:35:43 2024

@author: partda1

Week 4 Lecture 2
MNIST DIGITS - Logistic Regression
"""

import numpy as np
import scipy.io
import pylab as plt

from sklearn.utils import shuffle as shuf
from sklearn.linear_model import LogisticRegression as logReg

########################################################################
### Loading data to memory
mat = scipy.io.loadmat("./data/mnist")
X_digits = mat['data'].T
y_digits = mat['label'][0].T
print("mat['label'][0]:  ",mat['label'][0])

########################################################################
### Looking at data shape
print("X_digits.shape :  ", X_digits.shape)
print("Unique entries of y_digits: ", np.unique(y_digits))
########################################################################
### Visualising 1st row of data matrix (X)
print("\nClass of first element in our data set: ", y_digits[0])
plt.rc("image", cmap="binary")
print("\nData shape of first row of X: \n", X_digits[0])
print("\nFirst row of X: \n", str(list(X_digits[0])))
print("\nTransforming the first row of X into a 2 dimensional representation: ")

# Transforming the first row of X into a 2 dimensional representation
plt.matshow(X_digits[0].reshape(28, 28)) #784 elements row  = a 28x28 matrix 28x28=784
ax = plt.gca() #Get current axes
ax.grid(False)

########################################################################
### Creating two classes for first numbers (0 and 1)

# Select element using Condition (numpy)
zeros = X_digits[y_digits==0]  #select all the rows of X where y (target value) is zero (i.e. the zero digits)
ones = X_digits[y_digits==1]
print("zeros.shape: ", zeros.shape)
print("ones.shape: ", ones.shape)

# Viewing plots of the data
plt.rc("image", cmap="binary")
#Zeros
plt.matshow(zeros[0].reshape(28,28))
ax = plt.gca()
ax.grid(False)
#Ones
plt.matshow(ones[0].reshape(28,28))
ax = plt.gca()
ax.grid(False)

########################################################################
### Rearranging the data
print("\nRearranging the data")
X_new = np.vstack([zeros, ones]) #vstack = stack the data for zeros/ones vertically
y_new = np.hstack([np.repeat(0, zeros.shape[0]), np.repeat(1, ones.shape[0])]) #stack horizontally
print("X_new.shape: ", X_new.shape)
print("y_new.shape: ", y_new.shape)
print("y_new: ", y_new)

#Shuffle the data
X_new, y_new = shuf(X_new, y_new)
X_mnist_train = X_new[:5000]
X_mnist_test = X_new[5000:]
y_mnist_train = y_new[:5000]
y_mnist_test = y_new[5000:]

# Learn/Fit a logistic regression model
logRegModel = logReg(solver='lbfgs')
logRegModel.fit(X_mnist_train, y_mnist_train)
print("logRegModel: ", logRegModel)

########################################################################
### Visualize the coefficients of the fitted model
print("\nVisualize the coefficients of the fitted model... (new plot)")
plt.matshow(logRegModel.coef_.reshape(28,28))
plt.colorbar()
ax = plt.gca()
ax.grid(False)

########################################################################
### Testing model/s accuracy : score
print("\nTesting model accuracy(score):")
print("Accuracy training set \t: ", logRegModel.score(X_mnist_train, y_mnist_train))
print("Accuracy test set \t\t: ", logRegModel.score(X_mnist_test, y_mnist_test)) #how well is logRegModel likely to perform in unseen data (~0.998)
 
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:00:31 2024

@author: devon

Week 4 Lecture 2
Logistic Regression

"""

import math
import matplotlib.pyplot as plt
import numpy as np
import pylab as plt

from sklearn.datasets import make_blobs as mb
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

########################################################################
### Logistic Regression

theta0 = 0
theta1 = 1

def sigmoid(x, t0, t1):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-(t0+t1*item))))
    return a

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x, theta0, theta1)
plt.plot(x, sig, linewidth=2)
plt.xlim([-10, 10])
plt.ylim([-0.02, 1.02])
plt.show()

X, y = mb(n_samples=100, n_features=2, centers=2, cluster_std=1.7, random_state=1) # Dataset consisting of two Gaussian clusters (100 data points)
print("X.shape: ", X.shape)
print("y: ", y)

plt.prism()
plt.scatter(X[:, 0], X[:, 1], c='b')
plt.show

logRegModel = LogisticRegression()

#Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

plt.prism()
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
plt.scatter(X_test[:, 0], X_test[:, 1], c='black', marker='^')

#Fit the data to the logistic regression model
logRegModel.fit(X_train, y_train)

#Display the model intercept and coefficient
print("\nLogReg Intercept: \t", logRegModel.intercept_)
print("LogReg Coefficient: ", logRegModel.coef_)

def plot_decision_boundary(clf, X):
    w = clf.coef_.ravel()
    a = -w[0] / w[1]
    xx = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]))
    yy = a * xx - clf.intercept_ / w[1]
    plt.plot(xx, yy)
    plt.xticks(())
    plt.yticks(())
y_pred_train = logRegModel.predict(X_train)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_pred_train)
plot_decision_boundary(logRegModel, X)

#Check accuracy of training set
print("\nAccuracy on training set: \t", logRegModel.score(X_train, y_train))

y_pred_test = logRegModel.predict(X_test)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_test, marker='^')
plot_decision_boundary(logRegModel, X)
print("Accuracy on test set: \t\t", logRegModel.score(X_test, y_test))

########################################################################
### Exercises

#New data blob - Cluster_STD increased to 8 - data blobs are closer together 
X, y = mb(n_samples=100, n_features=2, centers=2, cluster_std=8, random_state=1)
print("X.shape (CSTD=8): ", X.shape)
print("y (CSTD=8): ", y)
y_pred_test = logRegModel.predict(X_test)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_test, marker='^')
plot_decision_boundary(logRegModel, X)



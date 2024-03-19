# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:30:36 2024

@author: partda1

Week 4 Lecture 1
Linear Regression with Multiple Variables [Feature Scaling]
"""
########################################################################
### Feature Scaling  (Standardise data with scikit learn)

from sklearn import preprocessing as pp
import numpy as np

np.set_printoptions(suppress=True) #Make output look cleaner
X = np.array([
    [ 1000, -1,  0.02],
    [ 1500,  2,  0.07],
    [ 1290,  1.5, -0.03]
    ])
print("X array data before processing:")
print(X)

X_scaled = pp.scale(X)
print("\nX preprocessed to X_scale:")
print(X_scaled) #Each column has a mean of 0 and a standard deviation of 1 

print("\nX_scaled MEAN:")
print(X_scaled.mean(axis=0))

print("\nX_scaled STANDARD DEVIATION:")
print(X_scaled.std(axis=0))

########################################################################
### Using preprocessing StandardScaler
X_train = X
scaler = pp.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
print("\nFirst 10 rows of X data (Standard Scalar): ")
print(X_train_scaled[:10])
print("Scaler MEAN: ", scaler.mean_) #Mean of each column
print("Scaler SCALE: ", scaler.scale_) #Per feature relative scaling of the data

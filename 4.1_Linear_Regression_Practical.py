# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:02:34 2024

@author: partda1

Week 2 Lecture 2
Linear Regression and Gradient Descent
"""

"""FROM LECTURE
from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
accuracy= reg.score(X_test)
"""

########################################################################
### Loading data features and targets
print("\nLOADING DATA")
from sklearn import datasets as ds
diabetes = ds.load_diabetes();
X = diabetes.data
y = diabetes.target
print(X.shape)
print(y.shape)

print("\nPATIENT DATA - AGE, SEX, BMI")
print(X[0:10,0:3]) #Print 10 patients data for the first 3 X features

print("\nPATIENT DATA - Y target values")
print(y[0:10])

########################################################################
### Split model ino training/test set
from sklearn.utils import shuffle
X, y = shuffle(X, y, random_state=1) #Shuffle the examples, because for some datasets the examples are ordered
print("\nCHECKING X,y SHAPE AFTER SHUFFLE")
print(X.shape)
print(y.shape)
X = X[:, 2] #Take all the rows in X but only the column with index 2
print(X.shape)

##Training set should generally be larger than the test set
print("\nSPLITTING X INTO TRAINING/TEST SETS")
train_set_size = 250
X_train = X[:train_set_size] #Get the first 250 rows
X_test = X[train_set_size:] #Remaining rows used for test
print(X_train.shape)
print(X_test.shape)

# Split y-vector into train/test sets
print("\nSPLITTING y INTO TRAINING/TEST SETS")
y_train = y[:train_set_size]
y_test =y[train_set_size:]
print(y_train.shape)
print(y_test.shape)

print("\nPLOTTING SETS AS SCATTER PLOTS")
import pylab as plt
plt.figure(1)
trainingDataScatterPlot = plt.scatter(X_train, y_train)
testDataScatterPlot = plt.scatter(X_test, y_test)
#Set axis labels and create key for data
plt.xlabel("Data")
plt.ylabel("Targets")
plt.legend((trainingDataScatterPlot, testDataScatterPlot), ("Training Data", "Test Data"))

########################################################################
### Sklearn linear regression models
from sklearn import linear_model as lm
linearRegressionModel = lm.LinearRegression()
#Reshape data as only tracking a single feature
linearRegressionModel.fit(X_train.reshape(-1, 1), y_train)
#Display coefficient (slope) and the bias (the intercept) of our linear model
print("Linear Regression coefficient: ", linearRegressionModel.coef_) 
print("Linear Regression intercept: ", linearRegressionModel.intercept_)

########################################################################
### Calculating mean square error on testset
import numpy as np
print("Training error: ", np.mean((linearRegressionModel.predict(X_train.reshape(-1, 1)) - y_train) ** 2))
print("Test error: ", np.mean((linearRegressionModel.predict(X_test.reshape(-1, 1)) - y_test) ** 2))
print("Output y prediction: ", linearRegressionModel.predict(np.array(0.04).reshape(1,-1))) #predicts output y using feature x of 0.04


########################################################################
### Ploting the linear model
plt.figure(2)
plt.scatter(X_train, y_train, color="blue")
plt.plot(X_train, linearRegressionModel.predict(X_train.reshape(-1,1)), color="red", linewidth=3)
plt.xlabel("Data")
plt.ylabel("Target")

plt.figure(3)
plt.scatter(X_test, y_test,  color='orange')
# Plots the linear model
plt.plot(X_test, linearRegressionModel.predict(X_test.reshape(-1, 1)), color='red', linewidth=3);
plt.xlabel('Data')
plt.ylabel('Target');

########################################################################
### Estimation of model accuracy
print("Model 'Score': ", linearRegressionModel.score(X_test.reshape(-1, 1), y_test))
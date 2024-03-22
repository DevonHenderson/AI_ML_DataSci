# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:17:12 2024

@author: devon

Week 4 Lecture 2
Glass.csv Practice Exercise - Logistic Regression

"""

import pandas as pd

from sklearn.linear_model    import LogisticRegression as LogReg
from sklearn.model_selection import train_test_split   as tts
from sklearn                 import preprocessing      as pPro
from sklearn.utils           import shuffle            as shuf

########################################################################
### 1) Load data from glass.csv
df = pd.read_csv("./data/glass.csv")             # df -> descriptive features
dataLoaded = True if 'df' in locals() else False # Set if data frame loaded to local memory
print("Ex 1) Data Loaded: ", dataLoaded)         # Console output of data loading successfully or not

########################################################################
### 2 & 3) Place predictors/target vector in variables X/y
X = df.iloc[:,1:10].values           # predictors placed in feature matrix (excl. id and household columns)
y = y = df['household'].values       # targets placed in vector y          (household column)
print("\nEx 2) X predictors in feature matrix: \n", X)
print("\nEx 3) y target vector set: \n", y)

########################################################################
### 4) Shuffle the data
print("\nEx 4) Shuffling the data: ")
print("X before shuffle: \t", X.shape)
print("y before shuffle: \t", y.shape)
X, y = shuf(X, y, random_state=1)
print("X after  shuffle: \t", X.shape)
print("y after  shuffle: \t", y.shape)

########################################################################
### 5) Splitting and scaling the data
print("\nEx 5) Splitting the Datasets: [X data scaled]")
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.25)   # 75% training data, 25% test data
scaler = pPro.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled  = scaler.transform(X_test)
print("Total X.shape before split\t: ", X.shape)
print(f"Train size = {X.shape[0]}*0.75 [75%] : ", X.shape[0]*.75 )
print(f"Test  size = {X.shape[0]}*0.25 [25%] : ", X.shape[0]*.25 )
print("----")
print("Results of Split: ")
print("X_train_scaled: ", X_train_scaled.shape)
print("X_test_scaled : ", X_test_scaled.shape)
print("y_train\t\t  : ", y_train.shape)
print("y_test\t\t  : ", y_test.shape)

########################################################################
### 6) Create Logisitic Regression model and fit the training data
logRegModel = LogReg()               # Create
logRegModel = LogReg(solver='lbfgs', max_iter=1000) # Assign solver and iterations
logRegModel.fit(X_train, y_train)                   # Fit training data
print("\nEx 6) Logisitc Regression Model fitted with data: ",logRegModel)

########################################################################
### 7) Testing model/s accuracy : score
print("\nEx 7) Testing model accuracy(score):")
print("Accuracy training set \t: ", logRegModel.score(X_train, y_train))
print("Accuracy test set \t\t: ",   logRegModel.score(X_test,  y_test ))
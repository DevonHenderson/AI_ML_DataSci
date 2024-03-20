# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:38:29 2024

@author: devon

Week 4 Lecture 1
Linear Regression -- Exercises 
"""

import numpy as np
import pandas as pd
import pylab as plt

from sklearn.utils import shuffle as shuf
from sklearn import linear_model as lm
from mpl_toolkits.mplot3d import Axes3D

########################################################################
### Loading housing dataset
df = pd.read_csv("./data/Housing.csv") # df -> descriptive features
print("Housing data read from CSV file: \n", df)

# Set mapping values for string CSV input data
mapping={'yes':1,'no':0} # Modify any values that are yes to =1, no to =0
mapping2={'furnished':2,'semi-furnished':1,'unfurnished':0} # Modify furnishingstatus values from string to int values

# Remap string values (yes/no) to 1/0
df['mainroad']  = df['mainroad' ].map(mapping)
df['guestroom'] = df['guestroom'].map(mapping)
df['basement']  = df['basement' ].map(mapping)
df['prefarea']  = df['prefarea' ].map(mapping)
df['hotwaterheating'] = df['hotwaterheating'].map(mapping)
df['airconditioning'] = df['airconditioning'].map(mapping)

# Remap furnishing string values to int
df['furnishingstatus'] = df['furnishingstatus'].map(mapping2)

#Display newly mapped data values
print("\nHousing Data (Mapped) df: \n", df)

########################################################################
### Extract next the feature matrix 'X' and target vector 'y' from the data frame df
y = df['price'].values
## print("\nTarget Vector values of df: ", y) #output excessively long in console
X = df.iloc[:,1:].values
print("df.iloc[:,1:] : \n", X)

########################################################################
### Exercise 1
### Shuffle the data
print("\n##################################################################################################")
print("\n\t\t\t\t\t\t\t\t\tEX 1.) Shuffling the data")
print("X before shuffle: ", X.shape)
print("y before shuffle: ", y.shape)
X, y = shuf(X, y, random_state=1)
print("Running Shuffle [X, y = shuf(X, y, random_state=1)]...")
print("X after shuffle: ", X.shape)
print("y after shuffle: ", y.shape)

########################################################################
### Exercise 2
### Split data into Train/Test sets
print("\n##################################################################################################")
print("\n\t\t\t\tEX 2.) Multivariable linear regression on the training data [plot]")
print("\nSplitting X training/test sets")
train_set_size = int(X.shape[0]/2)
print("Train set size: ", train_set_size)
X_train = X[:train_set_size, :]
X_test = X[train_set_size:, :]
print("X_train.shape: ", X_train.shape)
print("X_test.shape: ", X_test.shape)

print("\nSplitting y training/test sets")
y_train = y[:train_set_size] # selects first 15 rows (targets) for train set
y_test = y[train_set_size:]  # selects from row 250 until the last one for test set
print("y_train set shape: ", y_train.shape)
print("y_test set shape: ", y_test.shape)

### Creating a linear regression model
print("\nCreating a linear regression model")
model_train = lm.LinearRegression()
model_test = lm.LinearRegression()
model_train.fit(X_train, y_train)# fit the model to the training set 
model_test.fit(X_test, y_test)# fit the model to the training set 
print("UNSURE WHAT EXPECTED RESULTS SHOULD LOOK LIKE. NO IDEA HOW TO PLOT 11 FEATURES TO A HYPERPLANE")

########################################################################
### Exercise 3
### What are the Coefficients of the model
print("\n##################################################################################################")
print("\n\t\t\t\t\t\t\t\tEX 3.) Coefficients and Intercept of the Model")
print("model.coef_ : \n", model_train.coef_)
print("\nmodel.intercept_ : \n", model_train.intercept_)  

########################################################################
### Exercise 4
### What is the mean squared error - both training and test set
print("\n##################################################################################################")
print("\n\t\t\t\t\t\t\t\tEX 4.) Mean Square errors of train/test sets")
print("Training Set: \t", np.mean((model_train.predict(X_train) - y_train) ** 2))
print("Test Set: \t\t", np.mean((model_test.predict(X_test) - y_test) ** 2))


########################################################################
### Exercise 5
### Coefficent of Determination
print("\n##################################################################################################")
print("\n\t\t\t\t\t\tEX 5.) Coefficent of Determination for Training and Test sets")
print("Training Model \tr2 score: ", model_train.score(X_train, y_train))
print("Test Model \t\tr2 score: ", model_test.score(X_test, y_test))

########################################################################
### Exercise 6
### Using model to predict price of 1st house in test set
print("\n##################################################################################################")
print("\n\t\t\t\t\t\tEX 6.) Predicting the price of the 1st house on the test set")
pred_price = model_train.predict([X_test[0]])
print("Predict price of 1st house in test set: ", pred_price)
print("Actual price of 1st house in test set: \t", y_test[0])

########################################################################
### Code used for results
print("\n##################################################################################################")
print("EXERCISES : SHORT ANSWERS")
print(#EX1
      "\nExercise 1): ", "X, y = shuf(X, y, random_state=1): ", 
      "\n----------------------------------------------------",
      "\nX.shape: \t\t\t", X.shape,
      "\ny.shape: \t\t\t", y.shape,
      )

print(#EX2
      "\nExercise 2): ", "train_set_size = int(X.shape[0]/2): ", 
      "\n----------------------------------------------------",
      "\nX.shape: \t\t\t", X.shape,
      "\nX_train.shape: \t\t", X_train.shape, 
      "\nX_test.shape: \t\t", X_test.shape, 
      "\ny.shape: \t\t\t", y.shape,
      "\ny_train set shape: \t", y_train.shape, 
      "\ny_test set shape: \t", y_test.shape
      )

#ChatGPT help for formatting Coefficents as seperate values in output
print(#EX3
      "\nExercise 3): ", "model.coef_, model.intercept_: ", 
      "\n----------------------------------------------")
coefficients = model_train.coef_
for i, coef in enumerate(coefficients):
    if i in range (10, 12):
        print(f'Coefficient {i}: \t({coef})')
    else:
        print(f'Coefficient {i}: \t\t({coef})')
print("Model Intercept : \t(", model_train.intercept_, ")")  

print(#EX4
      "\nExercise 4): ", "np.mean((model_train//test.predict(X_train//test) - y_train//test) ** 2): ", 
      "\n------------------------------------------------------------------------------------------",
      "\nTraining Set: \t\t", np.mean((model_train.predict(X_train) - y_train) ** 2),
      "\nTest Set: \t\t\t", np.mean((model_test.predict(X_test) - y_test) ** 2)
      )

print(#EX5
      "\nExercise 5): ", "model_train//test.score(X_train//test, y_train//test): ", 
      "\n------------------------------------------------------------------------------------------",
      "\nTraining Model \tr2 score: ", model_train.score(X_train, y_train),
      "\nTest Model \t\tr2 score: ", model_test.score(X_test, y_test)
      )

print(#EX6
      "\nExercise 6): ", "pred_price = model_train.predict([X_test[0]]): ", 
      "\n------------------------------------------------------------------------------------------",
      "\nPredict price of 1st house in test set: ", pred_price,
      "\nActual price of 1st house in test set: \t", y_test[0]
      )


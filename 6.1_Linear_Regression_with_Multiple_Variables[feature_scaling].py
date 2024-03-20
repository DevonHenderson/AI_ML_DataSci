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
    [ 1290,  1.5, -0.03]])
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
print("Scaler MEAN: ", scaler.mean_)   #Mean of each column
print("Scaler SCALE: ", scaler.scale_) #Per feature relative scaling of the data

#Use scaler instance on new data
X_test = np.array([
    [ 1100, -2,  0.03],
    [ 1200,  0.3,  -0.04],
    [ 1050,  1.4, -0.01]])
X_test_scaled = scaler.transform(X_test)
print("\nX_test scaled: ")
print(X_test_scaled)

########################################################################
### Multivariate Linear Regression
## Loading the Data

data = np.loadtxt("data/artifical_lin.txt")
print("\nData from Artifical_Lin - Parkinsons Telemonitoring: ")
print(data)

## Selecting data to visualise in 3D
X = data[:, :-1]# select all the rows [:, in the data object and all the columns except the last one ,:-1
y = data[:, -1] # select all the rows in the last column of the data object
print("\nPrint X[:10, :]\n", X[:10, :])
print("\nPrint y[:10] \n", y[:10])

## Shuffling the data
print("\nShuffling the data")
from sklearn.utils import shuffle as shuf
print("X before shuffle: ", X.shape)
print("y before shuffle: ", y.shape)
X, y = shuf(X, y, random_state=1)
print("X after shuffle: ", X.shape)
print("y after shuffle: ", y.shape)

########################################################################
### Splitting the data

# Split data into Train/Test sets
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

## Using Scikit-learn to split sets
from sklearn.model_selection import train_test_split as tts
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.5) #0.5 = 50%

########################################################################
### Plotting the data
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D

## Plot in 3D (View 1)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter3D(X_train[:, 0], X_train[:, 1], y_train[:],c='r')
ax.view_init(29,-15) #specifying the position from which we look at the data (i.e. perspective)
plt.xlabel(r'Voice feature 1 ($x_1$)',size=13)
plt.ylabel(r'Voice feature 2 ($x_2$)',size=13)
ax.set_zlabel('Clinician score of the patient symptoms')
plt.show()

## Plot in 3D (View 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter3D(X_train[:, 0], X_train[:, 1], y_train[:],c='r')
ax.view_init(200,50) #specifying the position in space from which we look at the data
plt.xlabel(r'Voice feature 1 ($x_1$)',size=13)
plt.ylabel(r'Voice feature 2 ($x_2$)',size=13)
ax.set_zlabel('Clinician score of the patient symptoms')
plt.show()

########################################################################
### Creating a linear regression model
print("\nCreating a linear regression model")
from sklearn import linear_model as lm
model = lm.LinearRegression()
model.fit(X_train, y_train)# fit the model to the training set (estimate the optimal parameters)
print("model.intercept_ : ", model.intercept_)  #Theta0
print("model.coef_ : ", model.coef_)    #Theta1, Theta2

### Evalutating success of model
print("Model Score: ", model.score(X_test, y_test)) #model explains around 80% 

### Mean square error
print("\nMean Square errors: ") # value of the cost function at the optimal parameters
print("Training Set: ", np.mean((model.predict(X_train) - y_train) ** 2))
print("Test Set: ", np.mean((model.predict(X_test) - y_test) ** 2))

########################################################################
### Plotting data and linear model
print("\nPlotting Data and Linear Model..") # plot the training data (marked as red dots) and the hyperplane representing our linear model
# Plotting the trained data
fig = plt.figure()
ax = Axes3D(fig)
ax = fig.add_subplot(111, projection="3d")
ax.scatter3D(X_train[:,0], X_train[:,1], y_train[:], c='r') # plots 3d points
range_x = np.linspace(X_train[:,0].min(), X_train[:,0].max(), num=10)
range_y = np.linspace(X_train[:,1].min(), X_train[:,1].max(), num=10)
xx, yy = np.meshgrid(range_x, range_y)
zz = np.vstack([xx.ravel(), yy.ravel()]).T
pred = model.predict(zz)
pred = pred.reshape(10,10)
plt.xlabel("Voice feature 1")
plt.ylabel("Voice feature 2")
ax.set_zlabel("Clinician score of the patient symptoms")
ax.plot_surface(xx, yy, pred, alpha=.3, color='b') # hyperplane shown as blue agains red training data
ax.view_init(20,-20)
plt.show()

# Plotting the test data
fig = plt.figure()
ax = Axes3D(fig)
ax = fig.add_subplot(111, projection="3d")
ax.scatter3D(X_test[:, 0], X_test[:, 1], y_test[:],c='b')    # plots 3d points 500 is number of points which are visualized
range_x = np.linspace(X_test[:, 0].min(), X_test[:, 0].max(), num=10)
range_y = np.linspace(X_test[:, 1].min(), X_test[:, 1].max(), num=10)
xx, yy = np.meshgrid(range_x, range_y)
zz = np.vstack([xx.ravel(), yy.ravel()]).T
pred = model.predict(zz)
pred = pred.reshape(10, 10)
plt.xlabel('Voice feature 1')
plt.ylabel('Voice feature 2')
ax.set_zlabel('Clinician score of the patient symptoms')
ax.plot_surface(xx, yy, pred, alpha=.3,color='r')  # plots the plane
ax.view_init(20,-20)
plt.show()

new_patient = model.predict([[0.4,0.9]]) # test the performance of your model with a new patient with example values
print("Model.prediction of example patient data [0.4, 0.9]: ", new_patient)

########################################################################
### Polynomial regression using nonlinear transformations
from sklearn.preprocessing import PolynomialFeatures as pf
X = np.array([0,2,4,6,7])
y = np.array([1,3,5,3,1])
plt.scatter(X,y)
poly = pf(degree=2)
X_transformed = poly.fit_transform(X.reshape(-1,1))
print("\nX_transformed: \n", X_transformed)
model = lm.LinearRegression() #linear model
model.fit(X_transformed,y)

X_test = np.array([1,3,5,8])  # Different data from initial training data arrays
X_test_transformed = poly.transform(X_test.reshape(-1,1))
y_predicted = model.predict(X_test_transformed)
print("\nX_test_transformed: \n", X_test_transformed)
print("y_predicted of X_test_transformed: ", y_predicted)

# Add to plot
plt.scatter(X,y, color='blue')
plt.scatter(X_test, y_predicted, color='red')
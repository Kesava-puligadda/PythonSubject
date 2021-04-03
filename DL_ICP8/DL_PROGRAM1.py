# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xkzQz0pvXbhCCaW6ZqVyAKIUG4UesPT5
"""

#Here import the required libraries
import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# Here we load the dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Here we fetch the diabetes files to get data
dataset = pd.read_csv("diabetes.csv", header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.27, random_state=79)
np.random.seed(161)
#Here we create a model
my_first_nn = Sequential() 
# Here we see hidden layer
my_first_nn.add(Dense(21, input_dim=8, activation='relu')) 
my_first_nn.add(Dense(61)) 
# This is the output layer below
my_first_nn.add(Dense(1, activation='sigmoid')) 
# compiling the assigned things here
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                    initial_epoch=0)
#print the results below
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
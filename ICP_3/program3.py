#start
import numpy as np

#importing the numpy here, if not install it or else throws error

Z = np.random.random_integers(2,12,15)

#assigning random integers to variable

print(Z)

#printing them

x = Z.reshape((3,5))

#Reshaping them into 3:5 ratio

print(x)

#printing after reshape

y = np.where(x == np.amax(x, axis=1, keepdims=True), 0, x)

print("After replacing the maximum no: in each row by 0")

print(y)
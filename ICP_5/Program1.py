import pandas as pd

import matplotlib.pyplot as plt

#Reading train.csv data from the file

train = pd.read_csv('train.csv')

#Display the scatter plot of GarageArea and SalePrice before deleting

plt.scatter(train.GarageArea, train.SalePrice, color='Red')

plt.xlabel('GarageArea')

plt.ylabel('SalePrice')

plt.show()

# calculate quarterly range

print(train.GarageArea.describe())

#Deleting the GarageArea outlier value

outlier_drop = train[(train.GarageArea >333) & (train.GarageArea <555)]

#Display the scatter plot after deleting of GarageArea and SalePrice

plt.scatter(outlier_drop.GarageArea, outlier_drop.SalePrice, color='Green')

plt.xlabel('GarageArea')

plt.ylabel('SalePrice')

plt.show()
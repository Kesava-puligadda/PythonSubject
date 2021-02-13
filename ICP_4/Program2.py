import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
glass = pd.read_csv('glass.csv')
x = glass[['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']]
y = glass['Type']

# create training and test parts

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

print("Shape of Training data")
print(X_train.shape, y_train.shape)

print("Shape of Testing data")
print(X_test.shape, y_test.shape)

clf = GaussianNB()
clf.fit(X_train, y_train)

print('Accuracy of Naive Bayes GaussianNB on training set:', round(clf.score(X_train, y_train)*100,2))
print('Accuracy of Naive Bayes GaussianNB on test set:', round(clf.score(X_test, y_test)*100,2))
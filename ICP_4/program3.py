from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

glass = pd.read_csv('glass.csv')

x = glass[['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']]
y = glass['Type']

# creating training and testing part

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

print("Shape of Training data")
print(X_train.shape, y_train.shape)

print("Shape of Testing data")
print(X_test.shape, y_test.shape)

svm = LinearSVC(random_state=0, tol=1e-5)
svm.fit(X_train, y_train)

print('Accuracy of SVM classifier on training set:', round(svm.score(X_train, y_train)*100,2))
print('Accuracy of SVM classifier on test set:', round(svm.score(X_test, y_test)*100,2))
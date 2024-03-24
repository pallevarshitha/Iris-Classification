# -*- coding: utf-8 -*-
"""Iris Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mbbv1r7zOGu9M23xAf7A2FAtYw5sov4s
"""

# Commented out IPython magic to ensure Python compatibility.

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline

iris = pd.read_csv('Iris.csv')

iris.head()

iris.info()

iris.drop(['Id','Species'], axis=1).describe()

iris['Species'].value_counts()

sns.pairplot(iris.drop(['Id'], axis=1),hue='Species')

import seaborn as sns
import matplotlib.pyplot as plt


sub = iris[iris['Species'] == 'Iris-setosa']


sns.kdeplot(data=sub[['SepalLengthCm', 'SepalWidthCm']], shade=True, color='plasma')


plt.title('Kernel Density Estimate for Sepal Length vs. Sepal Width (Iris-setosa)')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt


sub = iris[iris['Species'] == 'Iris-setosa']

sns.kdeplot(data=sub[['PetalLengthCm', 'PetalWidthCm']], shade=True, color='plasma')


plt.title('Kernel Density Estimate for Petal Length vs. Petal Width (Iris-setosa)')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')


plt.show()

sub_virginica=iris[iris['Species']=='Iris-virginica']

plt.scatter(sub_virginica['SepalLengthCm'], sub_virginica['SepalWidthCm'], marker='o', color='r')
plt.xlabel('Sepal Length Cm')
plt.ylabel('Sepal Width Cm')
plt.title('Sepal Width versus Length for virginica species')

from sklearn.model_selection import train_test_split
X=iris.drop(['Species', 'Id'], axis=1)
y=iris['Species']
X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.5, shuffle=True,random_state=100)

from sklearn.svm import SVC
model=SVC(C=1, kernel='rbf', tol=0.001)
model.fit(X_train, y_train)

pred=model.predict(X_test)
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
print(confusion_matrix(y_test, pred))
print('\n')
print(classification_report(y_test, pred))
print('\n')
print('Accuracy score is: ', accuracy_score(y_test, pred))

sepal_length = float(input("Enter sepal length (cm): "))
sepal_width = float(input("Enter sepal width (cm): "))
petal_length = float(input("Enter petal length (cm): "))
petal_width = float(input("Enter petal width (cm): "))
# Predict the class for the user input
new_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(new_data)


print("Predicted species:", prediction[0])


import pandas as pd
import numpy as np
import torch as tp
from sklearn.datasets import load_iris
import random
from sklearn import svm
#First we load the dataset 
data = load_iris()
print(data['feature_names'])
#We transfrom it into a data frame
df = pd.DataFrame(data['data'],columns=data['feature_names'])
df['setosa'] = df["sepal length (cm)"] * 0

#Print the first 10 examples from our df and the second row
print(df.head(10))
print(df.loc[1])

#With iloc and loc you can acces rows and collumns 
#the main dif between them is that with iloc you acces rows,column,elemnts 
#without knowing the name of the column/row and while you use loc you usually know the column you want to acces
#  [[]] returns you a df 
print(df.iloc[1:10])
print(df.iloc[1,2]) #first row third column
print(df.iloc[0:,0:4]) # all rows and 4 columns
print(df.loc[:,'sepal length (cm)']) # all the elemtns from sepal length (cm) column
print('/n')

train_data = df.iloc[0:75,0:4]
test_data = df.iloc[75:,0:4]
print(train_data,test_data)


clf = svm.SVC(gamma=0.001,C=100.)
clf.fit(data.data[:-1], data.target[:-1])

print(clf.predict(data.data[-1:]))

X = df
y = pd.Series(data.target,name='Species')
print(y)


#spliting the data into 2 parts the training one and the test ibe
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#here we aply on our data a linear model:logistic regression
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score

#we test the model on the data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acuratețea modelului: {accuracy}")

#visual plot
import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(X.assign(Species=y.map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})), hue='Species')
plt.show()

#all times you work with git pull commit push
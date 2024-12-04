import pandas as pd
import numpy as np
import torch as tp
from sklearn.datasets import load_iris
import random
#First we load the dataset 
data = load_iris()
print(data['feature_names'])
#We transfrom it into a data frame
df = pd.DataFrame(data['data'],columns=data['feature_names'])
df['setosa'] = df["sepal length (cm)"] * 0

#Print the first 10 examples from our df and the second element
print(df.head(10))
print(df.loc[1])

#With iloc and loc you can acces rows and collumns from your df
#  [[]] returns you a df
#the main dif between them is with iloc
print(df.iloc[1:10])
#print(df.loc[["sepal length (cm)"]])

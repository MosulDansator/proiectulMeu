import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(speed) # all numbers accumulated / len(speep)
median = np.median(speed) # is the number in the middle after you sort the list
commonValue = stats.mode(speed) # the most common value 
standardDeviation = np.std(speed) #means how spread out the values are from the mean 
percenti = np.percentile(speed,75) #percentile 75 means grouped with 75% of the members
print(mean,median,commonValue,standardDeviation)

#points spread on map formated from two axes x and y 
#every point is reprezented by a dataset
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()

x = np.array(x).reshape(-1,1)
y = np.array(y)
# Împărțirea datelor
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2)

#Model creation
model = LinearRegression()
model.fit(X_train, Y_train)

# We predict the model accuracy
predictions = model.predict(X_test)

# Vizualizare
plt.scatter(x, y, color='blue')
plt.plot(x,model.predict(x), color='red')
plt.show()
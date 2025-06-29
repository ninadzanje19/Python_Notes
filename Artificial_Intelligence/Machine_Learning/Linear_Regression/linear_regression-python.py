import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

house_data = pd.read_csv("USA_Housing.csv")

#print(house_data.head())
#print(house_data.info())
#print(house_data.describe())
#print(house_data.columns)


#Training a LINEAR REGRESSION MODEL
#X and Y arrays
X = house_data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
Y = house_data['Price']

#Train Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=101)

"""
test_size is the amount of % of data set to be used for testing
X are our features
Y is our target i.e. what we are trying to predict
y = mx + c
The value of y is dependent upon the change in x
"""

#Creting and training the model

#Create a Linear Regression Object
lm = LinearRegression()
#Fit the training data on the model, this trains the model
lm.fit(X_train, Y_train)

#Model Evaluation
###print(lm.intercept_)
#create a dataframe of coefficients
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
########print(coeff_df)

#Prediction from our Model
predictions = lm.predict(X_test)
plt.scatter(Y_test, predictions)

"""
The predict method takes in the parameters (X_test) and predict the target (Y_test) based upon it. 
Then we check our predictions in comparison to the actual values (Y_test) to see how good is our algorithm as well as 
our dataset
"""

"""
#Regression Evaluation Metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, predictions))
print('Mean Square Error:', metrics.mean_squared_error(y_test, predictions))
print('Root Mean Square Error*:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
"""


plt.show()

print("X_train")
print(X_train)
print("X_test")
print(X_test)
print("y_train")
print(Y_train)
print("y_test")
print(Y_test)
print("Predict Y_test on the basis of X_test")
print(predictions)

print(metrics.mean_absolute_error(Y_test, predictions))
print(metrics.mean_squared_error(Y_test, predictions))
print(np.sqrt(metrics.mean_squared_error(Y_test, predictions)))
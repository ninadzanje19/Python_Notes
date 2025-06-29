import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns                                                                                                   #import libraries

###############################################################################################################################################################################################################################################################

data = pd.read_csv("fake_reg.csv")                                                                                      #read the csv

###############################################################################################################################################################################################################################################################

from sklearn.model_selection import train_test_split                                                                    #import sklearn
X = data[["feature1", "feature2"]].values                                                                               #what we'll use to predict also known as 'Features'
Y = data[["price"]].values                                                                                              #what we want to predict also kknown as 'lables'

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)                        #Split the data into training and testing data
                                                                                                                        #test size denotes the % of data used for testing, the rest will be used for training
                                                                                                                        #random state decides which rows will be selected from the dataset
###############################################################################################################################################################################################################################################################


from sklearn.preprocessing import MinMaxScaler                                                                          #Scale the data. Only the features are scaled
scaler = MinMaxScaler()                                                                                                 #Scaling the maps all the data points between 0 and 1.
scaler.fit(X_train)                                                                                                     #fit() calculates the parameters required to perform the actual scaling

X_train = scaler.transform(X_train)                                                                                     #transform and replace the existing datasets
X_test = scaler.transform(X_test)

###############################################################################################################################################################################################################################################################

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


"""
model = Sequential([Dense(4, activation="relu"), Dense(4, activation="relu"), Dense(1)])                                #Not preffered
"""

model = Sequential()                                                                                                    #create a model of sequential type
model.add(Dense(4, activation="relu"))                                                                                  #Dense is the type of Neural Network where each node of a layer is conencted to every other node of the subsequent layer
model.add(Dense(4, activation="relu"))                                                                                  #relu (Rectified Linear Unit) is the activation function used
model.add(Dense(4, activation="relu"))
model.add(Dense(1))                                                                                                     #The number of nodes in the final layer determine the number of outputs. In this case it is a single value the price
                                                                                                                        #The value of the output is compared with the values in the labels by using the loss function
model.compile(loss="mean_squared_error", optimizer="rmsprop")                                                           #Complie the model #loss is the loss function used, optimizer is the method of performing the gradient descent

"For multi-layer classification problem use loss = categorical_crossentropy"
"For binary classification use loss = binary_crossentropy"
"For regression problem use loss = mse (mean_squared_error)"

model.fit(x=X_train, y=Y_train, epochs=250)                                                                             #train the model, x is the features to be trained, y is the labels the features to be trained, epochs number of times the network will be run iteratively

loss = pd.DataFrame(model.history.history)                                                                              #gives a dict of the losses and casts them into a df

model.evaluate(x=X_test, y=Y_test, verbose=0)                                                                           #get the amount of loss occured upon fitting of this dataset. In this case it is rms, therefore well get the root of the mean of the squares of the error
model.evaluate(x=X_train, y=Y_train, verbose=0)

test_predictions = model.predict(X_test)                                                                                #predicts the values of the labels

"""
Since the values of the lables have been predicted we can now compare it with the actual values of the labels and infere towards a conclusion. We can tweake the Neural Network to our nedds to derive the desired values
"""

model.save("My_Model.h5")                                                                                               #Model can be saved in .keras format or .h5 format. In .h5 the weights are saved


new_data = [[500, 400]]
new_data = scaler.transform(new_data)                                                                                   #predictions can be made upon the new data but it has to be scaled first
model.predict(new_data)

from tensorflow.keras.models import load_model
new_model = load_model("My_Model.h5")                                                                                   #loads an existing model
new_predictions = new_model.predict(new_data)                                                                           #The existing model once loaded can be used to predict upon any other dataset
print(new_predictions)
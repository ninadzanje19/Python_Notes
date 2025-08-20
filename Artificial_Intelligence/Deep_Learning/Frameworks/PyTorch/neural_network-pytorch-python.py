import pandas as pd
import torch
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error

#load the data as a dataframe
data = pd.read_csv("fake_reg.csv")
df = pd.DataFrame(data)

x = df[['price', 'feature1']].values                            #What we take into consideration while we predict
y = df[['feature2']].values                                             #What we predict


scaler = StandardScaler()                                            #Scale x to the values of y
x_scaled = scaler.fit_transform(x)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Convert data to PyTorch Tensors
# The data types (dtype) are important!
X_train_tensor = torch.tensor(x_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32) # Use float32 for regression and BCE loss
X_test_tensor = torch.tensor(x_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32)

#Define the TabularDataset class. This transforms our raw data into data processable by PyTorch.
class TabularDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def __len__(self):
        # This should return the total number of samples
        return len(self.features)

    def __getitem__(self, idx):
        # This should return one sample and its corresponding label
        # The DataLoader will call this method to create batches
        item_features = self.features[idx]
        item_label = self.labels[idx]
        return item_features, item_label

#Create your training set and testing set as objects of the TabularDataset
train_dataset = TabularDataset(X_train_tensor, y_train_tensor)
test_dataset = TabularDataset(X_test_tensor, y_test_tensor)

BATCH_SIZE = 64

# Here we are creating an instance of the DataLoader. The arguments we give are dataset to train on, batch size and shuffling
train_loader = DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)

#Batching - We break the dataset into small chunks (batches) and then process it.
#Shuffle - Shuffle the order of data in the batch. This is to avoid the patterns.

test_loader = DataLoader(dataset=test_dataset, batch_size=BATCH_SIZE, shuffle=False)
#During evaluation, we are not training the model or updating its weights. We are simply measuring its performance.


device = "cuda" if torch.cuda.is_available() else "cpu"

#In PyTorch the schema of the Neural Network is defined by a SimpleNeuralNetwork class
class RegressionModel(nn.Module):
    #Cunstructor of the Neural Network Class
    def __init__(self, input_features, output_features):
        super().__init__()

        #Define the layers of the Neural Network
        self.network = nn.Sequential(
            #First layer takes 'input_features' as the input and gives 64 output values
            nn.Linear(input_features, 64),
            nn.ReLU(),  #Apply the Activation Function

            #Second layer takes the 64 input values from the previous layer and gives 32 output values
            nn.Linear(64, 32),
            nn.ReLU(),  # Apply the Activation Function

            #Final (Output) layer takes the 32 input values from the previous layer and maps them to 'output_features'
            #The final layer gives out the output, so it does not have any Activation Function
            nn.Linear(32, output_features)
        )

    #Define the function that controls the flow through the Neural Network
    def forward(self, x):
        # The forward pass is simple: just pass the input through our network.
        return self.network(x)



input_size = x_train.shape[1]  #Number of input features
output_size = y_train.shape[1] #Number of output features

#Instantiate the model as an object of the Neural Network class
model = RegressionModel(input_features=input_size, output_features=output_size).to(device)

#Define the loss function
loss_fn = nn.MSELoss()

#Define the Optimizer
learning_rate = 1e-3 # 0.001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

#Define the number of epochs
num_epochs = 5000

# The main training loop
for epoch in range(num_epochs):
    # Set the model to training mode.
    model.train()

    # This will keep track of the loss for this epoch
    epoch_loss = 0.0

    # Loop over each batch of data from the train_loader
    for batch_features, batch_labels in train_loader:
        # Move the data to the correct device (CPU or GPU)
        batch_features = batch_features.to(device)
        batch_labels = batch_labels.to(device)

        # --- The 5 Core Steps of Training ---


        outputs = model(batch_features)      #1. Forward Pass: Pass the features through the model to get predictions.
        loss = loss_fn(outputs, batch_labels)#2. Calculate Loss: Compare the model's predictions (outputs) to the true labels.
        optimizer.zero_grad()                #3. Zero the Gradients: Reset the optimizer's gradients from the previous step.
        loss.backward()                      #4. Backward Pass (Backpropagation): Calculate the gradients of the loss.
        optimizer.step()                     #5. Update Weights: Tell the optimizer to update the model's weights using the gradients.

        epoch_loss += loss.item()# Add the loss from this batch to our running total for the epoch

    # After looping through all batches, you can get the average loss for the epoch
    avg_epoch_loss = epoch_loss / len(train_loader)


model_path = "My_Model.pth"
torch.save(model.state_dict(), model_path)

input_size = x_train.shape[1]
output_size = y_train.shape[1]

loaded_model = RegressionModel(input_features=input_size, output_features=output_size).to(device)

loaded_model.load_state_dict(torch.load(model_path))
loaded_model.eval()
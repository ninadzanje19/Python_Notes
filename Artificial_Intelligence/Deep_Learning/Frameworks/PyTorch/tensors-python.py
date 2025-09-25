"""Everything in PyTorch is built around the torch.Tensor.
Think of it as the PyTorch equivalent of a NumPy array.
It's a multidimensional grid of numbers."""

import torch

# Create a tensor from a Python list
my_list = [[1, 2], [3, 4.5]]
tensor = torch.tensor(my_list)

# Create a tensor of a specific shape, filled with random numbers
shape = (2, 3,)
rand_tensor = torch.rand(shape)

# Create a tensor of all ones or zeros
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

tensor_shape = tensor.shape                     #Get the shape of the tensor
tensor_type = tensor.dtype                      #Get the data type of the tensor
tensor_device = tensor.device                   #Get the device on which the tensor is stored

tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

# Element-wise operations (+, -, *, /)
tensor_addition = tensor1 + tensor2
tensor_subtraction = tensor1 - tensor2
tensor_multiplication = tensor1 * tensor2
tensor_division = tensor1 / tensor2

#Push the tensor to GPU
gpu_tensor = tensor.to("cuda")

#Push the tensor to CPU
cpu_tensor = tensor.to("cpu")
tensor = cpu_tensor

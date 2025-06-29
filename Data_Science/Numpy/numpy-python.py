"""#################################NumPy Notes###############################################"""

import numpy as np

my_list = [1, 2, 3]
#create an 1D array of list
arr = np.array(my_list)

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#create an matrix of 2D list
matrix = np.array(my_matrix)

#create an array of values from (start, end-1, interval)
arange = np.arange(0, 10)

arange_interval = np.arange(0, 11, 2)

#create an Array of 0 with size (size)
zero_array = np.zeros(3)

#create an Matrix of 0 with size (row, col)
zero_matrix = np.zeros((5, 5))

#create an Array of 1 with size (size)
one_array = np.ones(3)

#create an Matrix of 1 with size (row, col)
one_matrix = np.ones((5, 5))

#create an Array from (start, end, no. of elements) with equal space
linspace = np.linspace(0, 10, 5)

#create an Identity Matrix
identity_matrix = np.eye(4)

#create an Array of random numbers of size (size)
random_array = np.random.rand(2)

#create a Matrix of random numbers of size (row, col)
random_matrix = np.random.rand(5, 5)

#create an Array of random numbers of size (size), not uniform
randn_array = np.random.randn(2)

#create a Matrix of random numbers of size (row, col), not uniform
randn_matrix = np.random.randn(5, 5)

#create an Array of random integers(min, max, no of elements), default no. of elements 1 for multidimensional array pass a tuple with dimensions
randint = np.random.randint(1, 100, 10)

my_array = np.arange(25)
#create a new array by converting the old array into an array[row, col]
my_matrix = my_array.reshape(5, 5)

#max value of an Array
max = my_matrix.max()
#position of max value of an Array
max_pos = my_matrix.argmax()
#min value of an Array
min = my_matrix.min()
#position of min value of an Array
min_pos = my_matrix.argmin()

#create a copy of an Array
slice_copy = my_array.copy()

#slice an Array from [start, end], new Array is a reference to old one. def start val = 0, def end val = arr.len()
slice = my_array[0:11]

#change all the values of an Array to the given value
slice_copy[:] = 99

#returns an Array with bool vals where True for cond satisfied else False
bool_array = slice > 5

#returns an Array where bool_array is True for corresponding values of slice
new_arr = slice[bool_array]

#perform operation on all the elements of the Array
add = my_array + 2

#gives sqrt of each element in the Array
sqrt = np.sqrt(my_array)

#For more Built in Functions and Methods check the documentation

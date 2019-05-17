# Array
# For Python, arrays can be seen as a more efficient way of storing 
# a certain kind of list.
# The elements of an array have to be of the same data type.

import array as arr

# The data type is specified during the array creation and specified using a tyoe code,
# which is a single character like the I used in the example below.

a = arr.array("I", [3,6,9])

print(type(a))
print('\n')

# List
# Used to store a collection of heterogeneous items
# Lists are mutable, which means you can change their content 
# without changing their identity.

x = [] # Empty list

print(type(x))

x1 = [1,2,3]

print(type(x1))

x2  = list([1, 'apple', 3])

print(type(x2))
print(type(x2[1]))

x2[1] = 'orange'
print(x2)

# Adding new items to a list
list_num = [1,2,45,6,7,2,90,23,435]
list_char = ['c', 'o', 'o', 'k', 'i', 'e']

list_num.append(11) # Add 11 to the list, by default adds to the last position
print(list_num)

list_num.insert(0, 11)
print(list_num)

list_char.remove('o')
print(list_char)

list_char.pop(-2) # Removes the item at the specified position
print(list_char)

list_num.sort() # In-place sorting
print(list_num)

list.reverse(list_num)
print(list_num)

print('\n')

# Arrays versus Lists
# Able to apply the tostring() function to array_char because Python is aware that
# all the items in the array are of the same data type and hence the operation behaves
# the same way on each element.
# Arrays can be useful when dealing with a large collection of homogeneous data types.
# Since Python does not have to remember the data type details of each element
# individually; for some uses arrays may be faster and uses less memory when compared
# to lists.
array_char = arr.array("u", ["c", "a", "t", "s"])
array_char.tostring()
print(array_char)
print('\n')

# NumPy arrays are heavily used to work with multidimensional arrays.
# They are more efficient than the array module and Python lists in general.
# Reading and writing elements in a NumPy array is faster, and they support "vectorized"
# operations such as elementwise addition. NumPy arrays also work efficiently well with
# large sparse datasets.

import numpy as np

arr_a = np.array([3, 6, 9])
arr_b = arr_a/3 # Performing vectorized (element-wise) operations
print(arr_b)

arr_ones = np.ones(4)
print(arr_ones)

multi_arr_ones = np.ones((3,4)) # Creating 2D array with 3 rows and 4 columns
print(multi_arr_ones)
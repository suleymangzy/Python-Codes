# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:33:35 2024

@author: SÜLEYMAN BEYYY
"""

#The Numpy library is added with the abbreviation name np as follows:
'''
import numpy as np 
'''
#Creating an array:
'''
import numpy as np 
array = np.array([1,2,3,4,5,6])
print(array)
'''
'''
Learning the data type of the array: The type of the above array is ndarray type, which is one of the numpy data types.
Like Python, the numpy library has its own data types. 
ndarray one of them.
'''
'''
import numpy as np 
array = np.array([1,2,3,4,5,6])
print(type(array))
'''
#Learning the type of data in the array: The data in the above array is int32 data type.
'''
import numpy as np 
array = np.array([1,2,3,4,5,6])
print(type(array.dtype))
'''
'''
The data type in Numpy is defined in the broadest sense: For example, the data type in an array is:
If there are both number and float types, the dtype value is set to float. Because it floats
The data type includes integers. In short, NumPy arrays, memory efficiency and performance
requires homogeneous data types, so only one data type is required for an array
defined.
'''
'''
import numpy as np 
array = np.array([1,2.5,3,4.8,10,23.6])
print(type(array.dtype))
'''
#Creating a two-dimensional array:
'''
import numpy as np 
array = np.array([[1,2,3],[4,5,6]])
print(array)
'''
#Learning how dimensional the arrays are:
'''    
import numpy as np 
array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array.ndim)
'''
#Learning the number of rows and columns of arrays:
'''
import numpy as np 
array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(array.shape)
'''
#Creating an array of different size from a single array:
'''
import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array)
print(array.shape)
print(array.reshape(4,3))
'''
#Automatic number sequence generation:
'''
import numpy as np
array = np.arange(10)
print(array)
print(array.ndim)
print(array.shape)
'''
#Automatic number sequence creation with fixed spacing:
'''
import numpy as np
array = np.arange(30,0,-3)
print(array)
'''
#Copying an array:
'''
import numpy as np
array = np.arange(10)
array1 = array.copy()
print(array1)
'''
#Creating an array of random numbers:
'''
import numpy as np
array = np.random.random(8)
print(array)
'''
#Creating a one-dimensional array of random integers:
'''
import numpy as np
array = np.random.randint(20,size=4)
print(array)
'''
#Create a two-dimensional array of 2-row, 4-column random numbers:
'''
import numpy as np
array = np.random.random((2,4))
print(array)
'''
#Create a two-dimensional array of 2-row, 4-column random integers:
'''
import numpy as np
array = np.random.randint(0,20,size=(2,4))
print(array)
'''
#Getting the first two lines of the array:
'''
import numpy as np
array = np.arange(8)
array = array.reshape(4,2) 
print(array)
print(array.ndim)
print(array.shape)
array1 = array[0:2]
print(array1)
print(array1.ndim)
print(array1.shape)
'''
#Getting the first column of the array:
'''
import numpy as np
array = np.arange(9)
array = array.reshape(3,3)
print(array)
print(array.ndim)
print(array.shape)
array1 = array[:,0] 
print(array1)
print(array1.ndim)
print(array1.shape)
'''
#Example of a matrix with 5 rows, 3 columns and zeros:
'''
import numpy as np
array = np.zeros((5,3))
print(array)
'''
#Example of a matrix consisting of three-dimensional 1s:
'''
import numpy as np
array = np.ones((2,3,4))
print(array)
'''
#Creating a 2*4 array with all 5 elements:
'''
import numpy as np 
array = np.ones((2,4))*5
print(array)
'''
#We can also use the full() method to create an array whose elements are the same. 
#(2,3) When specifying the size, creating the matrix from 8's:
'''
import numpy as np
array = np.full((2,3),8)
print(array)    
'''
#Example of creating an identity matrix:
'''
import numpy as np
array = np.eye(3)
print(array)
'''
#Matrix combining example:
'''
import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
matrix1 = np.array([[7,8,9],[10,11,12]])
combining = np.concatenate([matrix,matrix1])
print(combining)
'''
#If the 'axis' value is used in matrix combination, the matrices are arranged side by side.
'''
import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
matrix1 = np.array([[7,8,9],[10,11,12]])
combining = np.concatenate([matrix,matrix1],axis=1)
print(combining)
'''
#Finding the maximum value of a series:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.max())    
'''
#Finding the minimum value of an array:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.min())    
'''
#Finding the sum of all values ​​in an array:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.sum())
'''
#Finding the sum of all rows in an array:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.sum(axis=1))
'''
#Finding the sum of all columns in an array:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.sum(axis=0))
'''
#Finding the average of all values ​​in an array:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.mean())    
'''
#Finding variance in a series:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.var())
'''
#Finding the standard deviation in a series:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.std())
'''

#Mathematical operations can be performed between arrays, but the size and shape of the arrays are
#It must be compatible with . That is, it must have the same number of rows and columns.
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6]])
array1 = np.array([[7,8,9],[10,11,12]])
print(array+array1)
print(array-array1)
print(array*array1)
print(array/array1)
print(array%array1)
print(array+10)
'''
#Trigonometric operations can also be performed on arrays.
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6]])
solution = np.sin(array)
solution1 = np.cos(array)
print(solution)
print(solution1)
'''
#The product of two matrices is calculated using the numpy.dot() function.
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6]])
array1 = np.array([[7,8],[9,10],[11,12]])
solution = np.dot(array,array1)
print(solution)
'''
#Transposition process:
'''
import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
transposition = matrix.transpose()
print(transposition)
'''
#Boolean operations on arrays and matrices:
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6]])
control = array < 4
print(control)
'''
#We can only array values ​​that satisfy the condition.
'''
import numpy as np
array = np.array([[1,2,3],[4,5,6]])
control = array[array < 4]
print(control)
'''

#.npy File Format:
'''
.npy, a file format that can be used to store and read NumPy arrays on disk
Supports files. .npy files are NumPy arrays in uncompressed binary format.
It is a file format in which it is saved. These files include save() and load() provided by NumPy.
It is created and read using functions. These files are high-performance data
Provides storage and transfer.
'''
#Additional info:
'''
NumPy also supports compressed files with the .npz extension. These files are
It can contain multiple .npy files and be stored as a compressed archive. these files
savez() and loadz() functions provided by NumPy for creating and reading
available.
'''
'''
import numpy as np
array = np.array([1,2,3,4,5,6])
np.save('test.npy',array) -> Let's save the array in a file named "test.npy".
new_array = np.load('test.npy') -> Let's load the data in the "test.npy" file into the variable named new_array.
print(new_array)
'''

#Extracting data from a .csv file:
'''
Numpy to read .csv files
You can use the numpy.genfromtxt() function. This function numpy a .csv file
It reads as a sequence. For example, the following contains data in a sample file named numbers.csv.
let's use it.
'''
'''
1,2,3
4,5,6
7,8,9
'''
'''
import numpy as np 
file_path = 'ornek.csv'
data = np.genfromtxt(file_path,delimiter=',')
print(data)
'''

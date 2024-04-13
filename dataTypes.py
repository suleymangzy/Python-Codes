# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:47:32 2024

@author: SÜLEYMAN BEYYY
"""

'''
            Variable Name Determination Rules
'''

# You cannot use the following words as variable names.
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del','elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal','not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
'yield']
'''
# These are words that have special meaning in Python.
# Additionally, if you wish, you can access the above list at any time by issuing the following commands:
'''
import keyword
print (keyword.kwlist)
'''
'''
In the Python programming language, the number of words we can specify as variable names is almost
It is unlimited. So we can use almost any word as a variable name. But still variable
There are some rules we need to pay attention to when determining the name. Some of these rules are mandatory, some are
It is a recommendation only.
'''
# 3_kilo_apples = 5 -> Variable names cannot start with a number.
# +value = 4568 -> Variable names cannot begin with arithmetic operators.
# _value = 4568 / value = 4568 -> Variable names must begin with an alphabet letter or the sign '_'.
# user name = '...' -> When determining variable names, no spaces can be left between the words that make up the variable.


'''
            Using Python Data Types to Create Arrays
'''

'''
Arrays are variables of identical data types declared under the same name. Using arrays,
Operation can be performed on multiple variable types with identical names.
'''

# List Data Type
'''
It allows combining multiple data arrays into a single type. Contains string, integer and float values
can accommodate.It is created with square brackets.
'''
# data =['...',19,20.50]

# Range Data Type
'''
Range actually works as a function. There is a numerical value between the entered values.
Creates a directory and gives output. It is generally used in loops (for, while, do while).
'''
'''
for i in range(10):
 print(i)
'''

# Tuple Data Type
'''
One of the collection types created by the array. The list structure cannot be changed differently
and are created sequentially. It works with parentheses.
'''
'''
data = ("Database", "Algorithm", "Web Programming")
print(data)
'''

'''
            Using Python Cluster Data Types
'''
#    Clusters
'''
It is used to hold multiple items in a single variable. The operating principle of clusters is also listed
like this. Both data types are used to hold variables. Field of use and quality among them
There are differences.
'''
'''
Clusters; It is a type of collection that is made sequentially and cannot be changed later.
Sets are written in curly brackets.
'''

# Set Data Type
'''
data2 = {"Audi", "Toyota", "Fiat"}
print(data2)
'''
'''
If we want to delete data from the cluster, we will need to apply the “remove” command.
'''
'''
data = {4,0,7,3}
sequencedata = set(data)
print(orderdata)
siraliveri.remove(0)
print(orderdata)
'''

# Frozenset Data Type
'''
Frozen clusters are called constrained and frozen clusters. as we know
Clusters were divided into two groups: modifiable and non-modifiable. Interchangeable sets: set
are sets. Invariant sets are frozen sets.
'''
'''
data = frozenset({"A",1,2,3,4,5})
print(data)
data.remove("A")
'''
'''
Since the created set is of a frozenset data type, data cannot be added or deleted.
If it gives an error, the change will not be applied to the cluster.
'''

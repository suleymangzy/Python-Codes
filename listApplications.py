# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:56:30 2024

@author: SÜLEYMAN BEYYY
"""

# Adding Elements to the List

'''
The append() method is used to add an element to the end of Python lists.
'''
'''
list1 = ["banana", "grape", "cherry"]
list1.append("apple")
print(list1)
'''
'''
The insert() method is used to add an element to a specified index in Python 
lists.
'''
'''
list1 = ["banana", "grape", "cherry"]
list1.insert(1,"apple")
print(list1)
'''

# Deleting an Element from the List

'''
There are different methods we can use to delete elements from Python lists.
We can use the remove() method to delete an element from the list.
'''
'''
list1 = ["banana", "grape", "cherry"]
list1.remove('cherry')
print(list1)
'''
'''
The pop() method is used to delete the element at a specified index in Python 
lists. If we do not specify an index number, the last element of the list is 
deleted.
'''
'''
list1 = ["banana", "grape", "cherry"]
list1.pop(1)
print(list1)
list1.pop()
print(list1)
'''
'''
We can delete the element at any index number with the del() method.
'''
'''
list1 = ["banana", "grape", "cherry"]
del list1[1]
print(list1)
'''
'''
If we do not give an index number to the del() method, it deletes the list as 
it is.
'''
'''
list1 = ["banana", "grape", "cherry"]
del list1
print(list1)
'''
'''
In this case, when we want to access the list object, we receive a NameError,
and in the description, we receive an error message stating that the list is 
not defined.
'''
'''
We can also delete the list with the clear() method, just as we delete the list
with the del command. However, the difference is that when we delete the object
reference with del and we get a NameError when we want to access the list, we 
do not get an error with the clear() method because the reference of the list 
continues to be in memory but it becomes empty.
'''
'''
list1 = ["banana", "grape", "cherry"]
list1.clear()
print(list1)
'''
'''
As you can see, the value [ ] returned to us by print(list) is the empty list 
definition. It still holds space in memory and we can continue to add elements 
to this list.
'''

# List Copy

'''
List is treated as a class and reference type in memory, so when we want to 
assign a list to another list, the list elements are not copied, instead the 
address information of the list in memory is copied.
'''
'''
list1 = ["banana", "grape", "cherry"]
list2 = ["banana", "grape"]
list1 = list2
print(list1)
list2.clear()
print(list1)
'''
'''
Therefore, there are some list methods we need to use when copying lists.
We can use the copy() method to assign the contents of a list to another list.
'''
'''
list1 = ["banana", "grape", "cherry"]
list2 = ["banana", "grape"]
list2 = list1.copy()
print(list2,list1)
list1.append('grape')
print(list2,list1)
'''

# Sorting List Elements

'''
The sort() method is used to sort the list elements.
'''
'''
numbers = [1, 10, 5]
letters = ['a', 'g', 's']
print(numbers)
print(letters)
numbers.sort() -> They are arranged numerically from smallest to largest.
letters.sort() -> Sorted alphabetically from a-z.
print(numbers)
print(letters)
'''
'''
When we want to sort in reverse, we can send the reverse=True parameter.
'''
'''
numbers = [1, 10, 5]
letters = ['a', 'g', 's']
print(numbers)
print(letters)
numbers.sort(reverse=True) -> They are listed in numerical order from largest 
                              to smallest.
letters.sort(reverse=True) -> Sorted alphabetically from z-a. 
print(numbers)
print(letters)
'''
'''
We can print list elements in reverse using the reverse() method.
'''
'''
numbers = [1, 10, 5]
letters = ['a', 'g', 's']
numbers.reverse()
letters.reverse()
print(numbers)
print(letters)
'''

#           Other List Methods

# Min() and Max() Method

'''
We can get the minimum and maximum value in a list numerically or 
alphabetically.
'''
'''
numbers = [1, 10, 5]
letters = ['a', 'g', 's']
print(min(numbers))
print(max(numbers))
print(max(letters))
print(min(letters)) 
'''

# Count() Method

'''
We use the count() method to get the number of repeating elements in a list.
'''
'''
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
print(numbers.count(10))
print(letters.count('a')) 
'''

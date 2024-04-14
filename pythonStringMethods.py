# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 05:01:06 2024

@author: SÜLEYMAN BEYYY
"""

# Split Method

'''
It performs fragmentation based on a character specified in the character string.
'''
'''
message = 'Hello, There.'
message = message.split(',')
print(message)
'''
'''
It sends us a list by splitting the string into pieces using the ',' character.
When we do not send a parameter to the split method, division is performed using the space character.
'''

# Upper Method

'''
Converts characters to uppercase.
'''
'''
message = 'hello there.'
message = message.upper()  
print(message)
'''
'''

** title(), The method converts the first letter of each word in the string to uppercase.
** The capitalize() Method capitalizes only the first letter of the first word in the string.
'''
'''
message = 'hello there.'
message1 = message.title()  
message2 = message.capitalize()
print(message1)
print(message2)
'''

# Strip Method

'''
The Strip method deletes whitespace characters at the beginning and end of the string.
'''
'''
username = '           .......          '
x = username.strip()
print('My username is {}'.format(x))
'''
'''
If we want the strip() method to delete the characters we specify, we need to send this character as a parameter.
'''
'''
username = '           .......!          '
x = username.strip()
y = x.strip('!')
print('My username is {}'.format(y))
'''

# Replacement Method

'''
The replace method is used to replace an expression in a character string.
'''
'''
message = 'My name is ...* .....'
message = message.replace('...*', '!!!')
print(message)
'''
'''
We can use replace() methods repeatedly. We can update Turkish characters, space characters and '@' sign in the url with the following expression.
'''
'''
url = '...'
url = url.replace(' ','-').replace('@','').replace('ö','o').replace('ü','u').replace('ş','s').replace('ü','u')
print(url)
'''

# Find Method

'''
The find method searches within the given string expression and returns the first index number it finds. If it can't find it, it returns an exception-1.
'''
'''
txt = 'My name is ... '
x1 = txt.find('...')
print(x1)
x2 = txt.find('...*')
print(x2)
'''

# Index Method

'''
The index method searches within the given string expression and returns the first index number it finds. If it cannot find it, it returns exception, unlike the find method.
'''
'''
txt = 'My name is ...'
x = txt.index('...')
print(x)
'''

'''
** We can also specify a search scope for the index and find method.
index("searched expression", "start index", "end index")/find("searched expression", "start index", "end index")
''' 
'''
txt = 'My name is ...'
x1 = txt.index('...',10,14)
x2 = txt.find('...',10,14)
print(x1)
print(x2)
'''

'''
website = "http://www.mehmetakif.edu.tr"
course = "Python Lesson: Start-to-End Python Programming Course (14 Weeks)"

print(website.count('a')) -> How many a characters are there in 'website'?
print(website.startswith('www')) -> Does “website” start with “www”?
print(website.startswith('http'))
print(website.endswith('com')) -> Does “website” end in 'com'?
print(website.endswith('.tr'))
print(course.isalpha()) -> Are the characters in 'course' all alphabetical?
print('hello'.isalpha())
print(course.isdigit()) -> Are all the characters in 'course' numeric?
print('123'.isdigit())
'''


'''
print('Contents'.center(50,'*')) -> There will be a total of 50 characters as ****Content****.
print('Contents'.ljust(50,'*')) -> There will be a total of 50 characters in the form, Content *********.
print('Contents'.rjust(50,'*')) -> There will be a total of 50 characters in the form ********* Contents.
'''















































# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:59:55 2024

@author: SÜLEYMAN BEYYY
"""

def primeNumber():
    number = int(input('Enter a number: '))
    counter = 0
    for i in range(2,number):
        if number % i == 0:
           counter += 1        
    if counter == 0:
       print('The number you entered is a prime number because it is only divisible by 1 and itself.')      
    else:
       print('The number you entered is not a prime number because it can be divided by numbers other than 1 and itself.') 
                    
primeNumber()         
            
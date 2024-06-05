# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:20:25 2024

@author: SÜLEYMAN BEYYY
"""
def oddEven():
   value = int(input('Enter a number between 0-20 ->'))
   
   if value < 0 or value > 20:
      while value < 0 or value > 20 :
           value = int(input('You entered an invalid number. Enter a number between 0-20 ->'))

   total = 0
   factorial = 1
   if value % 2 != 0:
     for i in range(1,value+1):
        factorial *= i     
     print(factorial)   

   else: 
       for i in range(value+1):
          if i % 2 == 0:
            total += i   
       print(total)   
            
oddEven()            
          
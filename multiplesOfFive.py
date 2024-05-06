# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:24:12 2024

@author: SÜLEYMAN BEYYY
"""

def multiplesOfFive():
    numbers = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
    for i in numbers:
        if i % 5 == 0 :
            print(i,',',end=' ')

multiplesOfFive()    
        
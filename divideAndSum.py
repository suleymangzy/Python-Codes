# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:25:27 2024

@author: SÜLEYMAN BEYYY
"""

def divideAndSum():
    SUM = 0
    for i in range(0,1000):
        if i % 9 == 0:
           SUM += i
    print('Sum:',SUM)       
            
divideAndSum()            
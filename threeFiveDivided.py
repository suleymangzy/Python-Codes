# -*- coding: utf-8 -*-
"""
Created on Sat May  4 02:20:32 2024

@author: SÜLEYMAN BEYYY
"""

def threeFiveDivided ():
    print('Numbers 1-100 that are divisible by three and five: ',end=' ')
    for i in range(1,101):
        if i%3==0 and i%5==0 :
            print(i,end=' ')

threeFiveDivided()

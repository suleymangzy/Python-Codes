# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:41:25 2024

@author: SÜLEYMAN BEYYY
"""

def horizontalPyramid():
    size = int(input('Size: '))
    for i in range(size+1):
        print('*'*i,end='')
        print()
    for i in range(size-1,0,-1):
        print('*'*i,end='')
        print()
        
horizontalPyramid()        
        
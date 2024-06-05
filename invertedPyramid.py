# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:57:34 2024

@author: SÜLEYMAN BEYYY
"""

def invertedPyramid():
    size = int(input('Size: '))
    for i in range(size,0,-1):
        print(' '*(size-i),end='')
        print('*'*(i*2-1))
            
invertedPyramid()            
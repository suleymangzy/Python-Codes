# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:51:10 2024

@author: SÜLEYMAN BEYYY
"""

def pyramid():
    size = int(input('Size: '))
    for i in range(size+1):
        print(' '*(size-i),end='')
        print('*'*(i*2-1))    
      
pyramid()        
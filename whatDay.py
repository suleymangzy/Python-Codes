# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:27:48 2024

@author: SÜLEYMAN BEYYY
"""

def whatDay():
    day = int(input('What day of the month are you on?\n->'))
    month = int(input('What month of the year are you in? (Enter numerically)\n->'))
    year = int(input('What year are you in?\n->'))
    year0 = [31,28,31,30,31,30,31,31,30,31,30,31]
    whatDay = day
    for i in range(month-1):
       whatDay += year0[i]
    if year % 4 == 0:
       whatDay += 1
    print('You are on the', whatDay ,'th  day of the year.')     
    
whatDay()    
    
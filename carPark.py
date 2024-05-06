# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:51:21 2024

@author: SÜLEYMAN BEYYY
"""

def carPark():
    time = int(input('How long was your vehicle parked in the parking lot?(Enter in hours)\n->'))
    
    shortTime = 10
    averageTime = 8
    longTime = 6
   
    if time < 1 :
       fee = shortTime
    elif time > 1 and time < 5 :
        fee = averageTime * time
    elif time > 5 :
        fee = longTime * time 
        
    print('Fee you need to pay: ',fee) 
   
carPark()




























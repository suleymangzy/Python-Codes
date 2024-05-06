# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:30:57 2024

@author: SÜLEYMAN BEYYY
"""

def pizza():
    preference = input('Press "S" key for small size, "M" key for medium size, "L" key for large size.\n->')
    extraCheese = input('Press the "Y" key if you want extra cheese, or the "N" key if you don\'t.\n->')
    extraDrink = input('If you want an extra drink, press the "Y" key, if not, press the "N" key.')
    
    fee = 0
    small = 25
    medium = 30
    large = 35
    drink = 2
    
    if extraCheese == 'Y':
        if preference == 'S':
            fee = small+2
        elif preference == 'M':
            fee = medium+3
        else:
            fee = large+3
    else:
        if preference == 'S':
            fee = small
        elif preference == 'M':
            fee = medium
        else:
            fee = large
   
    if extraDrink == "Y":
       fee += drink
            
    print('Fee you need to pay: ',fee)   
    
pizza()    
        
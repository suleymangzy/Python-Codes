# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:00:06 2024

@author: SÜLEYMAN BEYYY
"""

def cinemaTheater():
    cinema = 15
    theater = 10
    discount = 1/2
    educationalBackground = input('If your education level is high school or above, press the \'Y\' key, otherwise press the \'N\' key.\n->')
    if educationalBackground == 'Y':
        preference = input('If the event you prefer is cinema, press "C" or if it is theater, press "T".\n->')
        if preference == 'C':
            print('Amount you need to pay: ', cinema * discount)
        elif preference == 'T':
            print('Amount you need to pay: ', theater * discount)
    else:
        preference = input('If the event you prefer is cinema, press "C" or if it is theater, press "T".\n->')
        if preference == 'C':
            print('Amount you need to pay: ', cinema)
        elif preference == 'T':
            print('Amount you need to pay: ', theater)

cinemaTheater()
   
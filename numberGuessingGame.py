# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 00:39:04 2024

@author: SÜLEYMAN BEYYY
"""

def numberGuessingGame():
   
   import random 
   request = input('Do you want to play? (y/n) ->') 
   while request == 'y':
       
        guess = int(input('Guess the value chosen by the computer between 1-100 ->'))
        reply = random.randint(1,101)
       
        while guess != reply :
             if guess > reply :
                 guess = int(input('Guess a smaller number ->'))
             else :
                 guess = int(input('Guess a larger number ->'))
        
        print('Congratulations...')

        request = input('Do you want to play? (y/n) ->')

numberGuessingGame()            
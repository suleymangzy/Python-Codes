# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 01:20:41 2024

@author: SÜLEYMAN BEYYY
"""

def multilevelNumberGuessingGame():
    import random
    hardLevel = 5
    easyLevel = 10
    
    request = input('Do you want to play? (y/n) ->') 
    while request == 'y':
    
          print('You have 5 rights at the difficult level and 10 at the easy level.')
          levelPreference = input('What is your level preference? (e,d) ->')
    
          guess = int(input('Guess the value chosen by the computer between 1-100 ->'))
          reply = random.randint(1,101)
          print(reply)
          if guess != reply :
            if levelPreference == 'e' :
               easyLevel -= 1
               while guess != reply and easyLevel != 0:
                    if guess > reply :
                      easyLevel -= 1
                      guess = int(input('Guess a smaller number ->'))
                    else:
                      easyLevel -= 1
                      guess = int(input('Guess a larger number ->'))
            else :
                hardLevel -= 1
                while guess != reply and hardLevel != 0:
                     if guess > reply :
                        hardLevel -= 1
                        guess = int(input('Guess a smaller number ->'))
                     else:
                        hardLevel -= 1
                        guess = int(input('Guess a larger number ->'))     
                
    
            if guess != reply and (hardLevel == 0 or easyLevel == 0):
              print('You lost...')
            elif guess == reply :
             print('You won...')
    
            request = input('Do you want to play? (y/n) ->') 

multilevelNumberGuessingGame()    
    
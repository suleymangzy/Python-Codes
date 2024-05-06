# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:01:17 2024

@author: SÜLEYMAN BEYYY
"""

def rockPaperScissors():
    import random
    playerResponse = int(input('Enter the number at the beginning of the object you want to select;\n1-Stone\n2-Paper\n3-Scissors\n->'))
    computerResponse = random.randint(1, 3)
    rightToPlay = 2
    score = {'Computer':0,'Player':0}
    objects = ['Stone','Paper','Scissors']
    
    while rightToPlay != 0 :
          if (playerResponse == 1 and computerResponse == 3) or (playerResponse == 2 and computerResponse == 1) or (playerResponse == 3 and computerResponse == 2):
              print('Player\'s choice: ',objects[playerResponse-1],' Selection of computer:',objects[computerResponse-1])
              print('You won...')
              rightToPlay -= 1
              score['Player'] += 1
              computerResponse = random.randint(1, 3)
              playerResponse = int(input('Enter the number at the beginning of the object you want to select;\n1-Stone\n2-Paper\n3-Scissors\n->'))
          elif (playerResponse == 1 and computerResponse == 2) or (playerResponse == 2 and computerResponse == 3) or (playerResponse == 3 and computerResponse == 1):    
              print('Player\'s choice: ',objects[playerResponse-1],' Selection of computer:',objects[computerResponse-1])
              print('You lost...')
              rightToPlay -= 1
              score['Computer'] += 1
              computerResponse = random.randint(1, 3)
              playerResponse = int(input('Enter the number at the beginning of the object you want to select;\n1-Stone\n2-Paper\n3-Scissors\n->'))   
          else:
              print('Player\'s choice: ',objects[playerResponse-1],' Selection of computer:',objects[computerResponse-1])
              print('Equal...')
              rightToPlay -= 1
              computerResponse = random.randint(1, 3)
              playerResponse = int(input('Enter the number at the beginning of the object you want to select;\n1-Stone\n2-Paper\n3-Scissors\n->'))
    
    print('Score;\nComputer: ',score['Computer'],' Player: ',score['Player'])  
    
    
    if score['Player'] > score['Computer']:
        print('Congratulations...')
    elif score['Player'] < score['Computer']:
        print('Sorry, try again...')    
    else:
        print('Equal, try again...')

rockPaperScissors()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:35:15 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd 
import matplotlib.pyplot as plt
#Creating data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
#Creat the data frame
df = pd.DataFrame({'x':x,'y':y})
#Creating a point chart
df.plot.scatter(x='x',y='y')
#Set a chat properties
plt.title('Point Chart')
plt.xlabel('x')
plt.ylabel('y')
#Show chart
plt.show()
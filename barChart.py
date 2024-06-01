# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:09:55 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd
import matplotlib.pyplot as plt
#Creating data
categories = ['A','B','C','D']
values = [20,10,15,25]
#Create the data frame
df = pd.DataFrame({'Categories':categories,'Values':values})
#Create a bar chart
df.plot(x='Categories',y='Values',kind='bar')
#Set chart properties
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
#Show chart
plt.show()

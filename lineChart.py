# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:00:41 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd
import matplotlib.pyplot as plt
#Creating data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
#Create the data frame
df = pd.DataFrame({'x': x, 'y': y})
#Create a line chart
df.plot(x='x', y='y', kind='line')
#Set chart properties
plt.title('Line Chart')
plt.xlabel('x values ')
plt.ylabel('y values')
#Show chart
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:21:11 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd 
import matplotlib.pyplot as plt
#Creating data
data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8]
#Create the data frame
df = pd.DataFrame({'Data':data})
#Creating a Historam chart
df.plot.hist()
#Set a chart properties
plt.title('Historam Chart')
plt.xlabel('Data')
plt.ylabel('Frequency')
#Show chart
plt.show()

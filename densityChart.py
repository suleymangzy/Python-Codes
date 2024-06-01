# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:08:09 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
#Creating data
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
#Create the data frame 
df = pd.DataFrame({'Data':data})
#Create a density chart
sns.kdeplot(data=df['Data'].to_numpy())
#Set a chart properties
plt.title('Density Chart')
plt.xlabel('Value')
plt.ylabel('Density')
#Show chart
plt.show() 
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:59:22 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd
import matplotlib.pyplot as plt
#Creating data
years = [2010, 2011, 2012, 2013, 2014]
data1 = [10, 15, 12, 8, 20]
data2 = [5, 8, 6, 10, 12]
#Creat the data frame 
df = pd.DataFrame({'Year':years,'Data1':data1,'Data2':data2})
#Create a area chart
df.plot.area(x='Year')
#Set a chart properties
plt.title('Area Chart')
plt.xlabel('Year')
plt.ylabel('Value')
#Show chart
plt.show()
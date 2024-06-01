# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:42:34 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd 
import matplotlib.pyplot as plt
#Creating data
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
#Create the data frame 
df = pd.DataFrame({'Data':data})
#Create a box chart
df.plot.box()
#Set a chart properties
plt.title('Box Chart')
plt.ylabel('Data')
#Show cahrt
plt.show()
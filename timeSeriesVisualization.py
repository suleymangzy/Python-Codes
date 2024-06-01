# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:54:45 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd
import matplotlib.pyplot as plt
#Create the time series dataset
data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
'2021-01-05'],
'Values': [10, 15, 12, 18, 20]}
#Create the data frame 
df = pd.DataFrame(data)
#Convert date column to time format
df['Date'] = pd.to_datetime(df['Date'])
#Set date column as index
df.set_index('Date', inplace=True)
#Visualizing time series data
df.plot()
#Set a visualiz prooeties
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Data')
#Show visualiz
plt.show()
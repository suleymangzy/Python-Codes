# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:48:26 2024

@author: SÜLEYMAN BEYYY
"""
import pandas as pd
import matplotlib.pyplot as plt
#Create data
sizes = [30, 25, 20, 15, 10] 
labels = ['A', 'B', 'C', 'D', 'E']
#Creta a pie chart
plt.pie(sizes,labels=labels)
#Set a chat properties
plt.title('Pie Chart') 
#Show chart
plt.show()
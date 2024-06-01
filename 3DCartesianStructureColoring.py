# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:39:06 2024

@author: SÜLEYMAN BEYYY
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
soa=np.array([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
Z,Y,Z,U,V,W=zip(*soa)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([0,4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.xaxis.label.set_color('r')
ax.yaxis.label.set_color('g')
ax.zaxis.label.set_color('b')
ax.xaxis.line.set_color('r')
ax.yaxis.line.set_color('g')
ax.zaxis.line.set_color('b')
colors=['r','g','b','r','r','g','g','b','b']
quivers=ax.quiver(Z,Y,Z,U,V,W, color=colors)
plt.show()
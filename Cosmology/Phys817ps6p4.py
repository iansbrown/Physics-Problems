# -*- coding: utf-8 -*-
"""
Created on Tue May  1 07:10:41 2018

@author: ibrow
"""

import numpy as np
import matplotlib.pyplot as plt

d = np.random.normal(99, 1.3, 1000)
b = np.random.normal(0, 0.725, 1000)
v = np.random.normal(0, 1000, 1000)

zcm = (70/300000)*d
zkin= v/300000
ztot= (1+zcm)*(1+zkin)-1


fig1=plt.figure()
plt.scatter (b,zcm,s=2, c='r', marker='+')
plt.xlabel('angular position',fontsize=16)
plt.ylabel('redshift',fontsize=16)    
plt.title('redshift vs angular position', fontsize=16)      

fig1=plt.figure()
plt.scatter (b,ztot,s=2, c='r', marker='+')
plt.xlabel('angular position',fontsize=16)
plt.ylabel('redshift',fontsize=16)    
plt.title('redshift vs angular position', fontsize=16) 


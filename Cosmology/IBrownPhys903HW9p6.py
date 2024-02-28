# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:40:04 2017
Physics 903 
Professor Dawn Erb
Problem set 6
Problem 6
@author: Ian Brown
"""

import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

#read velocity.dat file
V=[]
for filename in ['velocities.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        V.append(float(line.split()[0]))

Vdat=np.array(V) 

#Define a maxwell distribution and fit to it
maxwell = stats.maxwell
params = maxwell.fit(Vdat, floc=0)

print('Scale Parameter a=',params[1])
m=1.008*1.66E-27
k=1.38064852E-23
T=(m*(params[1])**2)/k
print ('Gas Temperature T=',T)
plt.hist(Vdat, bins=30, normed=True,color='green')
x = np.linspace(0, 45000, 1000)
plt.plot(x, maxwell.pdf(x, *params), lw=3)
plt.xlabel('Velocity m/s',fontsize=16)
plt.ylabel('Number Density',fontsize=16)    
plt.title('Maxwell-Boltzmann Distribution', fontsize=16)
plt.show()
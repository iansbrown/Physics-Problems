# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:50:40 2017
Physics 903 
Professor Dawn Erb
Problem set 6
Problem 1
@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt

Yeff=[]
Vrot=[]
#read dat file
for filename in ['yeff_vrot.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        Yeff.append(float(line.split()[1])) 
        Vrot.append(float(line.split()[2]))
        
#convert lists to arrays
y=np.array(Yeff)
v=np.array(Vrot) 
logy=np.log10(Yeff)

plt.scatter(v,logy)
plt.plot(v,0*v-1.9)
plt.xlabel('Rotational Velocity km/s',fontsize=16)
plt.ylabel('Effective Yield',fontsize=16)    
plt.title('expected yield vs rotational velocity', fontsize=16)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ianbrown
Phys 903 
HW 4 problem 5
Instructor Patrick Brady
"""

import numpy as np
import matplotlib.pyplot as plt

xmin=0
xmax=np.linspace(2,52,50,dtype=int)
N=np.linspace(50,1000,50,dtype=int)
M=np.empty((0))
rms=np.empty((0))
val=1.803085354
for k in range (0,50):
    x=np.random.uniform(xmin,xmax[5],N[k])
    for i in range(0,99):        
        F=x**2/(np.exp(x)+1)
        J=((xmax-xmin)/N)*np.sum(F)
        M=np.append(M,J)
    ms=((M-val)/val)**2
    rms=np.append(rms,np.sqrt((1/len(M))*np.sum(ms)))
    print (rms)
    
plt.plot(N,rms)
plt.ylabel('e(xmax,N)',fontsize=14)
plt.xlabel('N',fontsize=14)
plt.title('N vs e(xmax,N) xmax=%s'%xmax[5],fontsize=14)
plt.savefig('IbrownHW4plot1.png')
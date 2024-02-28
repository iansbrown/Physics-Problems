# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:50:40 2017
Physics 903 
Professor Dawn Erb
Problem set 6
Problem 5
@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt

Mtot=10**10
z=0
dZ=[0]
Z=[0]
x=np.logspace(0,9,200)

Mstar=x*9
Mgas=Mtot-Mstar
frac=Mgas/Mtot


dz=(-(0.02*(Mgas[0]-Mtot))/Mgas[0])
dZ.append(dz)
z=z+dz
Z.append(z)

for i in range (1,199):
    dz=(-(0.02*(Mgas[i]-Mgas[i-1]))/Mgas[i])
    dZ.append(dz)
    z=z+dz
    Z.append(z)
print (x,Mstar,Mgas,frac, dZ,Z)
print (len(Mstar), len (dZ),len(Z))
#plot
plt.plot(frac,Z,'r.',label='model')
plt.plot(frac,(0.02*np.log(1/frac)),label='calculated')
plt.legend()
plt.legend(bbox_to_anchor=(0.85, 0.8),bbox_transform=plt.gcf().transFigure)
# label axes
plt.xlabel('Gas Fraction',fontsize=16)
plt.ylabel('Metallicity',fontsize=16)    
plt.title('Metalicity vs Gas Fraction', fontsize=16)
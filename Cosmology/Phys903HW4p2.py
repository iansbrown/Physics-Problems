# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:06:31 2017
Physics 903 
Professor Dawn Erb
Problem set 4
Problem 2
@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt

#assign given values 
alphaMW=-1
alphaVirgo=-1.24
MbMW=-21
MbVirgo=-21

M=np.linspace(-23,-12,100)

Imw=(10**(0.4*(alphaMW+1)*(MbMW-M)))*np.exp(-10**(0.4*(MbMW-M)))
Ivirgo=(10**(0.4*(alphaVirgo+1)*(MbVirgo-M)))*np.exp(-10**(0.4*(MbVirgo-M)))

logMW=np.log(Imw)
logVirgo=np.log(Ivirgo)
offset1=np.min(logMW)
offset2=np.min(logVirgo) 

plt.plot (M,(logMW-offset1),'-g',label='Milky Way')
plt.plot (M,(logVirgo-offset2),'-b',label='Virgo Cluster')
plt.legend()
plt.legend(bbox_to_anchor=(0.9, 0.3),bbox_transform=plt.gcf().transFigure)
plt.xlabel('Magnitude blue band',fontsize=16)
plt.ylabel('Number Density per Magnitude',fontsize=16)    
plt.title('Schechter Luminosity Function', fontsize=16)
plt.savefig('Hw4Prob3')
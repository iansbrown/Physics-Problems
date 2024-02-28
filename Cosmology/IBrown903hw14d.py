# -*- coding: utf-8 -*-
"""
Spyder Editor
Author Ian Brown
Physics 903
HW1
Problem 4 d
Written 1/31/17
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#Constants
L=1 #luminosity
flux=[] #stores Fmin at each distance in array
NDensity=[] #number density array

#random star field with 10000 stars 
x=np.random.uniform (-1000,1000,10000)
y=np.random.uniform (-1000,1000,10000)
z=np.random.uniform (-1000,1000,10000)
l=np.random.uniform (1,5,100000) # giving each point a luminosity between 1 and 5
  
#for each star distance d calculate min flux and count stars inside the radius
for d in range (500,1,-5):
    N=0
    for i in range (0,10000):
        Fmin=6/(math.pi*4*d**2)
        r=((x[i]**2)+(y[i]**2)+(z[i]**2))**0.5
        F=l[i]/(math.pi*4*r**2)
        if F>=Fmin:
            N+= 1
    if N>=100:
        flux.append(Fmin)     
        NDensity.append(N)

#plotting
logF=np.log10(flux)
logN=np.log10(NDensity)
m, b = np.polyfit(logF, logN, 1)
bestfit = [m * i + b for i in logF]
print ("slope equals:" ,m)
plt.loglog (flux,NDensity, 'r+',logF,bestfit,'g-')
plt.autoscale(enable=True, axis='both')
plt.show()
   
        
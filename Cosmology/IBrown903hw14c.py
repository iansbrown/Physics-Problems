# -*- coding: utf-8 -*-
"""
Spyder Editor
Author Ian Brown
Physics 903
HW1
Problem 4 c
Written 1/31/17
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#Constants
L=3 #luminosity
flux=[] #stores Fmin at each distance in array
NDensity=[] #number density array

#random star field of 100000 stars 1000^3 volume
x=np.random.uniform (-500,500,100000)
y=np.random.uniform (-500,500,100000)
z=np.random.uniform (-500,500,100000)
   
#for each star distance d calculate min flux and count stars inside the radius
for d in range (500,1,-10):
    N=0
    for i in range (0,100000):
        Fmin=L/(math.pi*4*d**2)
        r=((x[i]**2)+(y[i]**2)+(z[i]**2))**0.5
        if r<=d:
            N+= 1
    if N>=200:
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
   
        
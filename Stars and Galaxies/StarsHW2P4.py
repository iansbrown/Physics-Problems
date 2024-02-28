#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:18:05 2018

@author: ianbrown
Phys 903 
HW 2 problem 4
Instructor Patrick Brady
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

M= np.array([23,16,10,7,4.5,3.6,3.1,2.7,2.3,1.9,1.6,1.4,1.25,1.03,0.91,0.83,0.77,0.72,0.67,0.62,0.56,0.5])
LogL=np.array([5.2,4.6,4.0,3.6,2.7,2.2,1.9,1.6,1.3,1.0,0.8,0.6,0.3,0.1,-0.1,-0.3,-0.5,-0.6,-0.7,-0.8,-0.9,-0.1])
Te=np.array([37000,30500,24000,17700,14000,11800,10500,9500,8500,7900,7350,6800,6300,5900,5540,5330,5090,4840,4590,4350,4100,3850])


R=np.sqrt((10**LogL)*6000**4/Te**4)
print (R)

def func(M,a,b):
    return b*np.log(M)+np.log(a)
y = M/R
print (y)
#popt,pcov=curve_fit(func,M,y)
a,b= poly.polyfit(np.log(M),np.log(y),1)
print (a,b)
#u,v=popt
#u=np.exp(a)
x=np.linspace(0,27,100)
u = np.exp(a)
print (u)
plt.plot(x,(np.exp(a)*x**b))
plt.scatter ((M),(y))

w=(10**LogL)/M
h,g= poly.polyfit(np.log(M),np.log(w),1)
alpha=g/-.844
print (alpha, g)
plt.scatter(M,w, color='red')
plt.plot (x,np.exp(h)*x**g, color='red')
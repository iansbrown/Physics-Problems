#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 02:28:03 2018
@author: ianbrown
Phys 903 
HW 5 problem 4
Instructor Patrick Brady
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func (x,a,b,c):
    #defines a function to fit
    return (a*np.exp(-((x-b)**2)/(2*c**2)))

#create list for data and populate from files
xdata1=[]
ydata1=[]
xdata2=[]
ydata2=[]

for filename in ['ps5_4a.txt']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        xdata1.append(float(line.split()[0]))
        ydata1.append(float(line.split()[1]))

for filename in ['ps5_4b.txt']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        xdata2.append(float(line.split()[0]))
        ydata2.append(float(line.split()[1]))

#use curve_fit to fit the data to the defined function
popt1,pcov1= curve_fit(func,xdata1,ydata1)
print (popt1)
A1,B1,C1=popt1

popt2,pcov2= curve_fit(func,xdata2,ydata2)
print (popt2)
A2,B2,C2=popt2
 
#plot data and fitted curve
plt.figure(1)
plt.scatter(xdata1,ydata1,color='blue')
plt.plot(xdata1,A1*np.exp(-(xdata1-B1)**2/(2*C1**2)),color='red')
plt.ylabel('Y',fontsize=14)
plt.xlabel('X',fontsize=14)
plt.title('Curve Fitting Data 1',fontsize=14)
plt.text(-30,10,'A=%s'%A1,fontsize=14)
plt.text(-30,9,'$\mu$=%s'% B1,fontsize=14)
plt.text(-30,8,'$\sigma$=%s'% C1,fontsize=14)

plt.savefig('IbrownHW5P4plot1.png')

plt.figure(2)
plt.scatter(xdata2,ydata2,color='blue')
plt.plot(xdata2,A2*np.exp(-(xdata2-B2)**2/(2*C2**2)),color='red')
plt.ylabel('Y',fontsize=14)
plt.xlabel('X',fontsize=14)
plt.title('Curve Fitting Data 2',fontsize=14)
plt.text(-18,6,'A=%s'%A2,fontsize=14)
plt.text(-18,5,'$\mu$=%s'% B2,fontsize=14)
plt.text(-18,4,'$\sigma$=%s'% C2,fontsize=14)
plt.savefig('IbrownHW5P4plot2.png')

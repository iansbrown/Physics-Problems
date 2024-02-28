# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:50:40 2017
Physics 903 
Professor Dawn Erb
Problem set 4
Problem 4
@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#read .dat file and store entries into lists.
Mdat=[]
binavg=[]

for filename in ['magnitudes.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        Mdat.append(float(line.split()[0]))
        
        
#convert lists to arrays
M=np.array(Mdat) 
#creat histogram data in bins
freq, bins = np.histogram(M, 100)
#make bins parameter into an array of same length as freq with median value of each bin.
for i in range (0,100):
    avg=(bins[i]+bins[i+1])/2
    binavg.append(avg)
avgbin=np.array(binavg)

def fit_func(avbin,a,b,c):
    return a*(10**(0.4*(b+1))*(c-avbin))*np.exp(-10**(0.4*(c-avbin)))
print (avgbin,freq)
popt,pcov=curve_fit(fit_func,avgbin,freq,p0=(150,-1,-19))
aa=popt[0]
bb=popt[1]
cc=popt[2]
print ('alpha=',bb,'phi=',aa,'Mstar=',cc) 

fig = plt.figure()
ax = fig.add_subplot(2,1,1)
histogram=ax.hist(M,100, facecolor='orange')
p=plt.plot(avgbin,fit_func(avgbin,aa,bb,cc),'b-')
ax.set_yscale('log')
plt.xlabel('Absolute Magnitude',fontsize=16)
plt.ylabel('Number Density',fontsize=16)    
plt.title('Luminosity Function', fontsize=16)
plt.savefig('LumFunc.png')
u# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 19:57:57 2017
Physics 903 
Professor Dawn Erb
Problem set 4
Problem 3
@author: Ian Brown
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#read .dat file and store entries into lists.
MassDense=[]
FormRate=[]
DynTime=[]

for filename in ['sf_gas_data.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        MassDense.append(float(line.split()[1]))
        FormRate.append(float(line.split()[2]))
        DynTime.append(float(line.split()[3]))
        
#convert lists to arrays
MD=np.array(MassDense) 
SFR=np.array(FormRate)
Dtime=np.array(DynTime)
#take log of Mass Density and SFR
logMD=np.log(MD)
logSFR=np.log(SFR)
m, b = np.polyfit(logMD, logSFR, 1)
bestfit = (m * logMD + b)
print('a=',m,'b=',b)
#part C
Mt=MD/Dtime
logMt=np.log(Mt)
def fit_func(logMt,c):
    return logMt+c
popt,pcov=curve_fit(fit_func,logMt,logSFR)
mean=np.mean(Dtime)
print ('intercept=',popt,'Mean dynamic time=',mean)

fig1=plt.figure()
ax = plt.gca()
ax.cla() # clear things for fresh plot

A=ax.plot(MD,SFR,'r+')
plt.xlabel('Gas mass density',fontsize=14)
plt.ylabel('Star Formation Rate',fontsize=14)    
plt.title('gas surface density vs SFR surface density', fontsize=14)

fig2=plt.figure()
B=plt.plot(logMD,logSFR,'r+',logMD,bestfit,'m-')
plt.xlabel('Gas mass density',fontsize=14)
plt.ylabel('Star Formation Rate',fontsize=14)    
plt.title('gas surface density vs SFR surface density(log)', fontsize=14)

fig3=plt.figure()
C=plt.plot(Mt,SFR,'b+')
plt.xlabel('Gas mass density per dynamic time',fontsize=14)
plt.ylabel('Star Formation Rate',fontsize=14)    
plt.title('gas surface density per dynamic time vs SFR surface density', fontsize=14)

fig4=plt.figure()
D=plt.plot(logMt,logSFR,'b+',logMt,fit_func(logMt,popt))
plt.xlabel('Gas mass density per dynamic time',fontsize=14)
plt.ylabel('Star Formation Rate',fontsize=14)    
plt.title('gas surface density per dynamic time vs SFR surface density', fontsize=14)
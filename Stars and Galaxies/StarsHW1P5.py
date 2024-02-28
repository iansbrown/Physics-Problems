#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:11:52 2018

@author: ianbrown
Phys 903 
HW 1 problem 5
Instructor Patrick Brady
"""

import matplotlib.pyplot as plt
import numpy as np

h=6.626e-34 #planck constant
k=1.38e-23 #boltzman constant
c=3.0e8 #speed of light
m=9.109e-31 #mass of electron

#Make array of temps
T1=np.logspace(0,np.log10(6.0e9),10, dtype=np.float128)
T2=np.logspace(np.log10(6.0e9),15,10, dtype=np.float128)


n1=((m*k*T1)/(h**2))**(3/2) #nQNR
n2=((k*T2)/(h*c))**3  #nQUR

Tc=T1*0+(m*(c**2)/k)
nc=n1*0+((m*c)/h)**3

plt.figure(figsize=(10,10)) 
ax = plt.axes(xscale='log', yscale='log')
plt.xlim(1e20,1e46)
plt.ylim(1e0,1e15)
plt.loglog(n1,Tc,'--',color='black')
plt.loglog(nc,T1,'--',color='black')
plt.loglog(n1,T1,'--',color='black')
plt.loglog(n2,T2,'--',color='black')
plt.xticks([1e25,1e30,1e35,1e40,1e45],fontsize=14)
plt.yticks([1e0,1e5,1e10,],fontsize=14)
plt.xlabel('ELECTRON CONCENTRATION ' r'$\mathit{n} \mathrm {(m^{-3})}$',fontsize=14)
plt.ylabel('TEMPERATURE T (K)',fontsize=14)
plt.text(1e22,1e14,'CLASSICAL, ULTRA-RELATIVISTIC\n' r'$P=nkT$',fontsize=14)
plt.text(2e20,8e8,'CLASSICAL, NON-RELATIVISTIC\n' r'$P=nkT$',fontsize=14)
plt.text(1e36,1e4,'DEGENERATIVE,\nULTRA-RELATIVISTIC\n' r'$P=K_{NR}n^{5/3}$',fontsize=14)
plt.text(1e28,1e3,'DEGENERATIVE,\nNON-RELATIVISTIC\n' r'$P=K_{NR}n^{5/3}$',fontsize=14)
plt.text(1e29,6e6,'Sun',fontsize=12)
plt.text(1e32,2e6,'White dwarf',fontsize=12,backgroundcolor='white')
plt.text(1e40,2e10,'Core of\nsupernova\nprogenitor',fontsize=12)
plt.text(1e26,5e0,'Normal Metal',fontsize=12)
#plt.show()
plt.savefig('IbrownHW1plot.png')
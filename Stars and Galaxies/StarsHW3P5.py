#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ianbrown
Phys 903 
HW 3 problem 5
Instructor Patrick Brady
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from astropy import units as u
from astropy import constants as const

#define mass of smaller white dwarf
M1=0.4*const.M_sun

def model(T,t):
    a=24*const.m_p*const.L_sun/(3*const.k_B*const.M_sun)
    dTdt=(-a)*((T/7e7)**(7/2))
    return dTdt

#set range of t and initial condition before calculating T(t)
t=np.linspace(1,1e10,10000)
T0=10**8
T=odeint(model,T0,t)

#initiate luminosity and calculate as a function of T and t
L1=[]
L2=[]
for i in range (len(T)):
    L1.append((3*const.k_B*T[i]*M1)/(5*t[i]*12*const.m_p))
    L2.append((3*const.k_B*T[i]*const.M_sun)/(5*t[i]*12*const.m_p))

# calculating R using 6.19 and 6.20
p1=(0.51/(0.5**5))*((0.4/1.85)**2)*(const.m_p/(const.h/(const.m_e*const.c))**3)
R1=(3*M1/(4*3.14159*p1))**(1/3)

p2=(0.51/(0.5**5))*((1/1.85)**2)*(const.m_p/(const.h/(const.m_e*const.c))**3)
R2=(3*const.M_sun/(4*3.14159*p2))**(1/3)

#use R and L to calculate surface temp
Teff1=(L1/(4*3.14159*(R1**2)*const.sigma_sb))**(1/4)
Teff2=(L2/(4*3.14159*(R2**2)*const.sigma_sb))**(1/4)

#calcukate average density and Debye Temp for each mass
rho1=M1/((4/3)*3.14159*R1**3)
rho2=const.M_sun/((4/3)*3.14159*R2**3)
TD1=1e7*(rho1/10**9)
TD2=1e7*(rho2/10**9)

# plotting 
plt.figure(figsize=(10,10)) 
plt.plot(L1[1:],Teff1[1:],label='0.4 Msun')
plt.plot(L2[1:],Teff2[1:],label='Msun')
horiz_line_data = np.array([TD1.value for j in range(len(L1))])
plt.plot(L2[1:], horiz_line_data[1:], 'r--')
horiz_line_data2 = np.array([TD2.value for j in range(len(L1))])
plt.plot(L2[1:], horiz_line_data2[1:], 'g--')
plt.xlabel('Luminosity ' ,fontsize=14)
plt.ylabel('Surface Temperature Teff (K)',fontsize=14)
plt.text(0.2e35,5.3e6,'TD=%e K'% TD2.value,fontsize=14)
plt.text(0.05e35,5.3e5,'TD=%e K'% TD1.value,fontsize=14)
plt.legend()
plt.savefig('IbrownHW3plot.png')
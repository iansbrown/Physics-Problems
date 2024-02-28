# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:14:30 2017

@author: Ian
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import astropy
from astropy import units as u#, constants as c
from astropy import cosmology as cosmo

# read in dat file redshift, distance modulus and sigma
z,mu,sigma = np.loadtxt('sn_z_mu_sigma.dat',usecols=(1,2,3),unpack=True)

X1=[]
X2=[]
X3=[]
Ho=67.3*u.km/u.s/u.Mpc

Om=np.linspace(0,1,100)
#for omega m only model:iterate through each omega m, calculate dL, distance modulus, and chi
for i in range(0,100):
    Lcosmo=cosmo.LambdaCDM(Ho,Om[i],0)
    dL=Lcosmo.luminosity_distance(z)
    mupred=5*np.log10(dL.value)+25
    Xa=(((mu-mupred)**2)/sigma**2)    
    X1.append(np.sum(Xa))
    
#Find reduced Chi, evaluate distance modulous using best fit omega m value.
cs1=np.array(X1)   
Xred1=cs1/40
LCDMcosmo=cosmo.LambdaCDM(Ho,Om[np.argmin(Xred1)],0)
dL1=LCDMcosmo.luminosity_distance(z)
mupred1=5*np.log10(dL1.value)+25

#plot omega m vs chi reduced
fig1=plt.figure()
plt.plot(Om,Xred1)
plt.xlabel('Matter Density',fontsize=16)
plt.ylabel('X Squared Reduced',fontsize=16)    
plt.title('Matter Only Fit Variation', fontsize=16)

#for flat universe model:iterate through each omega m, calculate dL, distance modulus, and chi
for i in range(0,100):
    Fcosmo=cosmo.FlatLambdaCDM(Ho,Om[i])
    dL=Fcosmo.luminosity_distance(z)
    mupred=5*np.log10(dL.value)+25
    Xb=(((mu-mupred)**2)/sigma**2)    
    X2.append(np.sum(Xb))
    
cs2=np.array(X2)   
Xred2=cs2/40

FLCDMcosmo=cosmo.FlatLambdaCDM(Ho,Om[np.argmin(Xred2)])
dL2=FLCDMcosmo.luminosity_distance(z)
mupred2=5*np.log10(dL2.value)+25

fig2=plt.figure()
plt.plot(Om,Xred2)
plt.xlabel('Matter Density',fontsize=16)
plt.ylabel('X squared reduced',fontsize=16)    
plt.title('Flat Universe Fit Variation', fontsize=16)


#for none flat matter and dark energy model
X3=np.zeros((100,100))
DE=np.linspace(0,1,100)
for i in range(0,100):
    for j in range(0,100):
        DEcosmo=cosmo.LambdaCDM(Ho,Om[i],DE[j])
        dL=DEcosmo.luminosity_distance(z)
        mupred=5*np.log10(dL.value)+25
        Xc=(((mu-mupred)**2)/sigma**2)    
        X3[i,j]=(np.sum(Xc))
    
    
print (X3)  
Xred3=X3/40
print (np.min(X3),np.argmin(X3,axis=0))
DEncosmo=cosmo.LambdaCDM(Ho,Om[0],DE[39])
dL3=DEncosmo.luminosity_distance(z)
mupred3=5*np.log10(dL3.value)+25

figc=plt.figure()
plt.contourf(Om,DE,Xred3)
plt.xlabel('Matter Density',fontsize=16)
plt.ylabel('Dark Energy Density',fontsize=16)    
plt.title('Chi Squared Contour', fontsize=16)


fig3=plt.figure()
plt.plot(z,mu,'+r')
plt.plot(z,mupred1,'.b')
plt.plot(z,mupred2,'.g')
plt.plot(z,mupred3,'.y')
plt.xlabel('Redshift z',fontsize=16)
plt.ylabel('Distance Modulus',fontsize=16)    
plt.title('Distance Modulus vs Redshift', fontsize=16)

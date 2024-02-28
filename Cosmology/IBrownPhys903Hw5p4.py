# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:42:35 2017
Physics 903 
Professor Dawn Erb
Problem set 5
Problem 4
@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.integrate as integrate

#read .dat file and store entries into lists.
obswave=[]
flux=[]
error=[]
obs=[]
fl=[]
er=[]
for filename in ['spSpec-51688-0302-325.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        obswave.append(float(line.split()[0]))
        flux.append(float(line.split()[1]))
        error.append(float(line.split()[2]))
        
#convert lists to arrays
obsw=np.array(obswave)
flx=np.array(flux)
err=np.array(error)

ob=np.max(obsw)
ab=np.min(obsw)

#exclude data outside wanted range
for i in range (0,3808):
    if obsw[i]>=4500.00 and obsw[i]<=8000.00:
        obs.append(obsw[i])
        fl.append(flx[i])
        er.append(err[i])
        
f=np.array(fl)
o=np.array(obs)
e=np.array(er)

#fit a line to subtract continuum
m,b=np.polyfit(o,f,1)
subf=f-(m*o+b)

#fit function summing 8 gaussians 
def fit_func(o,aa,bb,cc,dd,ee,ff,gg,hh,c,z):
    return ((aa*np.exp(-((o-(4862.721*(1+z)))**2)/(2*c**2)))+(bb*np.exp(-((o-(4960.295*(1+z)))**2)/(2*c**2)))+(cc*np.exp(-((o-(5008.239*(1+z)))**2)/(2*c**2)))+(dd*np.exp(-((o-(6549.86*(1+z)))**2)/(2*c**2)))+(ee*np.exp(-((o-(6564.614*(1+z)))**2)/(2*c**2)))+(ff*np.exp(-((o-(6585.27*(1+z)))**2)/(2*c**2)))+(gg*np.exp(-((o-(6718.29*(1+z)))**2)/(2*c**2)))+(hh*np.exp(-((o-(6732.68*(1+z)))**2)/(2*c**2))))

#get best fit parameters 
popt,pcov=curve_fit(fit_func,o,subf,p0=(35,32,82,5,95,10,15,10,7,0.025),sigma=e,absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
print ('HB amplitude(',(4862.721*(1+popt[9])),')',popt[0],'+/-',perr[0])
print ('OIII amplitude(',(4960.295*(1+popt[9])),')',popt[1],'+/-',perr[1])
print ('OIII amplitude(',(5008.239*(1+popt[9])),')',popt[2],'+/-',perr[2])
print ('NII amplitude(',(6549.86*(1+popt[9])),')',popt[3],'+/-',perr[3])
print ('Ha amplitude(',(6564.614*(1+popt[9])),')',popt[4],'+/-',perr[4])
print ('NII amplitude(',(6585.27*(1+popt[9])),')',popt[5],'+/-',perr[5])
print ('SII amplitude(',(6718.29*(1+popt[9])),')',popt[6],'+/-',perr[6])
print ('SII amplitude(',(6732.68*(1+popt[9])),')',popt[7],'+/-',perr[7])
print ('line width',popt[8],'+/-',perr[8])
print ('redshift',popt[9],'+/-',perr[9])

fig1=plt.figure()
ax = plt.gca()
plt.plot(o,fit_func(o,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5],popt[6],popt[7],popt[8],popt[9]))
plt.xlim(4900,5200)
ax.set_aspect(0.75)
fig2=plt.figure()
axx = plt.gca()
plt.plot(o,fit_func(o,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5],popt[6],popt[7],popt[8],popt[9]))
plt.xlim(6650,6950)
axx.set_aspect(0.75)
#10−17ergs−1cm−2 ̊A−1

#intergrate over h alpha then calculate flux, luminosity, star formation rate,
# velocity dispersion, and galactic Mass.
intgauss = lambda x: popt[4]*np.exp(-((x-(6564.614*(1+popt[9])))**2)/(2*popt[8]**2))
Falpha=integrate.quad(intgauss,6700,6750)
lum=Falpha[0]*4*np.pi*(3.302*10**26)
SFR=lum*7.9*10**(-42)
kms=popt[8]*(299792.458/(6564.614*(1+popt[9])))
sigtru=(kms**2-50**2)**0.5
M=(5*sigtru*0.8)/(4.3*10**(-6))

#print results
print ('flux =',Falpha[0])
print('luminosity=',lum)
print('star formation rate=',SFR)
print('velocity dispersion=',kms)
print ('true velocity dispersion=',sigtru)
print('Galactic Mass=',M)


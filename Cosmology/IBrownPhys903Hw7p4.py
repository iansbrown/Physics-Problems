# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:57:07 2017
Physics 903 
Professor Dawn Erb
Problem set 7
Problem 4
@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

redwl=[]
redflux=[]
#read dat file
for filename in ['spSpec-51820-0400-608.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        redwl.append(float(line.split()[0])) 
        redflux.append(float(line.split()[1]))
        
bluewl=[]
blueflux=[]
#read dat file
for filename in ['spSpec-51612-0280-549.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        bluewl.append(float(line.split()[0])) 
        blueflux.append(float(line.split()[1]))
        
filtwl=[]
transmission=[]
#read dat file
for filename in ['i_filter.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        filtwl.append(float(line.split()[0])) 
        transmission.append(float(line.split()[1]))
 
#convert to arrays       
rwl=np.array(redwl)
rflux=np.array(redflux)
bwl=np.array(bluewl)
bflux=np.array(blueflux)
fwl=np.array(filtwl)
tran=np.array(transmission)

#print (len(rwl),len(bwl),len(fwl))
#plot spectrum and tranmission curve
fig1=plt.figure()
plt.plot (rwl,rflux,'r',bwl,bflux,'b',fwl,500*tran,'-')
plt.xlim(3000,10000)
plt.xlabel('Rest Wavelength(Angstrom)',fontsize=16)
plt.ylabel('Flux',fontsize=16)    
plt.title('Rest-Frame Spectrum', fontsize=16)

#interpolate the transmission curve for wavelength array of blue and red galaxy
tranr=np.interp(rwl,fwl,tran)
tranb=np.interp(bwl,fwl,tran)
fr=rflux*(rwl**2)/2.99792458E+18
fb=bflux*(bwl**2)/2.99792458E+18
         
#integrate to get filter spectrum
intr= fr*tranr*rwl
intr1= tranr*rwl
frfilt=integrate.simps(intr,x=rwl)/integrate.simps(intr1,x=rwl)
intb= fb*tranb*bwl
intb1= tranb*bwl
fbfilt=integrate.simps(intb,x=bwl)/integrate.simps(intb1,x=bwl)

#get true magnitude
mrt=-2.5*np.log10(frfilt)-48.6
mbt=-2.5*np.log10(fbfilt)-48.6
print ("red true magnitude",mrt,'blue true magnitude',mbt)

#apply redshift z=0.85
rwlz=rwl*1.85
bwlz=bwl*1.85
#interpolate the transmission curve for wavelength array of blue and red galaxy
tranrz=np.interp(rwlz,fwl,tran)
tranbz=np.interp(bwlz,fwl,tran)
frz=rflux*(rwlz**2)/2.99792458E+18
fbz=bflux*(bwlz**2)/2.99792458E+18
         
#integrate to get filter spectrum
intrz= frz*tranrz*rwlz
intrz1= tranrz*rwlz
frzfilt=integrate.simps(intrz,x=rwlz)/integrate.simps(intrz1,x=rwlz)
intbz= fbz*tranbz*bwlz
intbz1= tranbz*bwlz
fbzfilt=integrate.simps(intbz,x=bwlz)/integrate.simps(intbz1,x=bwlz)

#get true magnitude
mro=-2.5*np.log10(frzfilt)-48.6
mbo=-2.5*np.log10(fbzfilt)-48.6
print ("red observered magnitude",mro,'blue observed magnitude',mbo)

#plot redshifted data
fig2=plt.figure()
plt.plot (rwlz,rflux,'r',bwlz,bflux,'b',fwl,500*tran,'-')
plt.xlim(6000,15000)
plt.xlabel('Rest Wavelength(Angstrom)',fontsize=16)
plt.ylabel('Flux',fontsize=16)    
plt.title('Reshifted Spectrum (z=.85)', fontsize=16)

Kr=mro-mrt
Kb=mbo-mbt
print ('K-correction(red)',Kr,'K-correction(blue)',Kb)
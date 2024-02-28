# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:14:25 2017
Physics 903 
Professor Dawn Erb
Problem set 3 
Problem 3
@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt
H_alpha=6562.85 #rest wavelength of Hydrogen alpha line
c=299792.46 #speed of light in Km/s
G=4.2*10**(-6) #G in Kpc(Km/s)^2/Msun
d=3000 #distance to galaxy in Kpc
conv=0.00029 #radians per arcminute

#read .dat file and store entries into lists.
obswave=[]
xarc=[]
yarc=[]

for filename in ['elliptical_stars.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        obswave.append(float(line.split()[1]))
        xarc.append(float(line.split()[2]))
        yarc.append(float(line.split()[3]))
        
#convert lists to arrays
obsw=np.array(obswave)
xarcm=np.array(xarc)
yarcm=np.array(yarc)
      
#print (obswave, xarc, yarc)
#print (obsw,xarcm,yarcm)

#calculate radial velocity from observed doppler shift
vrad=((obsw-H_alpha)/H_alpha)*c #velocity in Km/s
#calculate distance from center of Galaxy
xdist=d*(xarcm*conv)#use small angle approximation to calculate distance in Kpc
ydist=d*(yarcm*conv)   
r=np.sqrt(xdist**2+ydist**2)
Re=np.median(r)

#Calculate mean velocity and standaard deviation
vmean=np.mean(vrad)
stdev=np.std(vrad)
M=2*(5*Re*stdev**2)/G

circle = plt.Circle((0, 0), Re, color='r', fill=False)
fig1=plt.figure()
ax = plt.gca()
ax.cla() # clear things for fresh plot

p=ax.scatter(xdist,ydist, c=vrad)
ax.axis([xdist.min(), xdist.max(), ydist.min(), ydist.max()])
ax.add_artist(circle)
ax.set_aspect('equal')
# label axes
plt.xlabel('x distance in kpc',fontsize=16)
plt.ylabel('y distance in kpc',fontsize=16)    
plt.title('Elliptical Galaxy', fontsize=16)
#colorbar
cb = fig1.colorbar(p,ax=ax)
cb.set_label('Radial Velocity km/s', rotation=270,fontsize=16, labelpad=20)
plt.savefig('radialVscatter.png')
#Histogram
fig2=plt.figure()
histogram=plt.hist(vrad, 50, normed=1, facecolor='green')
plt.title('Radial Velocity Histogram', fontsize=16)
plt.savefig('radialVHist.png')
print('Size(kpc)=',Re)
print('mean velocity(km/s)=', vmean)
print('standard deviation=',stdev)
print ('Mass(Solar Masses)=',M) 
#!/usr/bin/env python

# start python with ipython --pylab
# to run: execfile('exponentialdisk.py')

import numpy as np
import matplotlib

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

fontsize=16
plt.rc('font',**{'family':'serif','serif':['Times']})
plt.rc('xtick',labelsize=fontsize)
plt.rc('ytick',labelsize=fontsize)
plt.rc('text',usetex=False)

# create image to be fit
# 2D exponential disk profile, symmetric in x and y
# disk is face-on

# parameters for our disk
# we will change the background and rms to see what happens
a = 5 # central surface brightness (flux per pixel)
h = 10 # scale length
b = 30 # background level

rms = 10 # standard deviation of gaussian noise added to image

def func(x, y, a, h, b):
    return a * np.exp(-np.sqrt(x**2 + y**2) / h) + b

x, y = np.mgrid[-50:50,-50:50]

z = func(x,y,a,h,b)

# add gaussian noise
zn = z + np.random.normal(0,rms,(100,100))

# clear figure window
plt.clf()

# get current figure
fig=plt.gcf()

# plot disk
p = plt.pcolor(x, y, zn, cmap='Greys')

# set range of plot to range of data
plt.axis([x.min(), x.max(), y.min(), y.max()])

# label axes
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)

# get current axes, so colorbar will know about them
ax=fig.gca()

# make colorbar
cb = fig.colorbar(p, ax=ax)
cb.set_label('Flux per pixel', rotation=270, size=fontsize, labelpad=20)

# now we fit for a, h, b
# we need to flatten the data
xydata = np.vstack((x.ravel(),y.ravel()))
zdata = zn.ravel()

# fit for the parameters in our function
popt, pcov = curve_fit(func, xydata, zdata)

print ('Best fit central surface brightness' + str('%3.2f' % popt[0]))
print ('Best fit scale length' + str('%3.2f' % popt[1]))
print ('Best fit background' + str('%3.2f' % popt[2]))

# circles showing best fit scale length, effective radius, r_95

hfit = popt[1]
r_e = 1.68 * hfit
r_95 = 4.74 * hfit

def circle(r,phi):
  return r*np.cos(phi), r*np.sin(phi)

phis = np.arange(0,2*np.pi,0.01)

ax.plot( *circle(hfit,phis), c='k',ls='-',linewidth=5)
ax.plot( *circle(r_e,phis), c='k',ls='--',linewidth=5)
ax.plot( *circle(r_95,phis), c='k',ls=':',linewidth=5)

savefig('exponentialdisk_fitc.pdf',transparent=True)

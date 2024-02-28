#!/usr/bin/env python

# this program makes and plots a 2D exponential disk
# the galaxy is seen face-on

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

fontsize=16
#plt.rc('font',**{'family':'serif','serif':['Times']})
#plt.rc('xtick',labelsize=fontsize)
#plt.rc('ytick',labelsize=fontsize)
plt.rc('text',usetex=False)

# create image to be fit
# 2D exponential disk profile, symmetric in x and y
# disk is face-on

a = 5 # central surface brightness (flux per pixel)
h = 10 # scale length
b = 0 # background level

rms = 0.1 # standard deviation of gaussian noise added to image

# define 2d exponential profile
def expdisk(x, y, a, h, b):
    return a * np.exp(-np.sqrt(x**2 + y**2) / h) + b

x, y = np.mgrid[-50:50,-50:50]

z = expdisk(x,y,a,h,b)

# add gaussian noise
zn = z + np.random.normal(0,rms,(100,100))

popt, pcov = curve_fit(expdisk, (x, y), zn, p0=5)
#print ('popt',popt)
#print ('pcov',pcov)
plt.figure()
# clear figure window
plt.clf()

# get current figure
fig=plt.gcf()

# plot disk
p=plt.pcolor(x, y, zn, cmap='Greys')

# set range of plot to range of data
plt.axis([x.min(), x.max(), y.min(), y.max()])

# label axes
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)

# get current axes, so colorbar will know about them
ax=fig.gca()

# make colorbar
cb = fig.colorbar(p, ax=ax)
cb.set_label('Radial Velocity', rotation=270, fontsize=16, labelpad=20)
#plt.show()
# save to PDF file (comment out for testing)
plt.savefig('exponentialdisk.png')

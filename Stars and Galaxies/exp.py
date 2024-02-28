# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:57:39 2017

@author: ibrow
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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

plt.figure()
plt.pcolor(x, y, zn, cmap='Greys')
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.savefig('exp.pdf')

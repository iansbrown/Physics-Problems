#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ianbrown
Phys 903 
HW 4 problem 1
Instructor Patrick Brady
"""

import numpy as np
import matplotlib.pyplot as plt

p=np.linspace(1e3,1e10,100)
T=8.4e9*(p/1e10)**(2/3)

plt.plot(p,T)
plt.ylabel('T fermi',fontsize=14)
plt.xlabel('density',fontsize=14)
plt.title('Density vs Fermi Temperature',fontsize=14)
plt.savefig('IbrownHW4P1plot1.png')
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 02:27:04 2017

@author: Ian Brown
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
#initialize variables and lists
a=[]
b=[]
f1=[]
a0=1
a.append(a0)
v=sp.Symbol ('v')

#calculate all the a sub j terms for series using recursion relation
for i in range (1,7):
    a.append((((i-1)-v)*(v+i)/(i**2))*a[i-1])
    
print (a)
#for add xi^n term to series
for k in range (0,7):
    b.append(a[k]*0.75**(k))
    
print(b)
#sum the terms and find roots
func=sum (b)#b[0]+b[1]+b[2]+b[3]+b[4]
print(func)
print (sp.solve(func,v))
#plot function over v=0,5
x=np.linspace (0,5,100)
for j in range (0,100):
    f1.append(func.subs(v,x[j]))
f=np.array(f1)
plt.plot(x,f,'b',x,0*x,'g')
plt.xlabel('v',fontsize=16)
plt.ylabel('P',fontsize=16)    
plt.title('Legendre ploynomial approximation for radial solution of cone point potential', fontsize=16)
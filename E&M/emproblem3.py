#Caitlin's attempt at problem 3 for E&M hw 4 

import math 
import sympy
from sympy import symbols 
from sympy import *

v,n,a,x = symbols('v n a x')
a=[]
Nterms=[1,2,3,4,5,6,7]
for n in Nterms:
     if n ==1:
          asubn = 1.0000
          a.append(asubn)
     else:
          asubn = ((((n-v)*(n+v+1))/((n+1)**2)))*a[n-2]*(3./4.)
 #         print a[n-2]
          a.append(asubn)
#print a
completeseries = sum(a)
#print completeseries
print solve(completeseries,v)

######################################
######################################
######################################
# 
# E&M PSET 4 Problem 3
#
# Danika Holmes
#
# Monday March 20, 2017
#
######################################
######################################
######################################

import math
import numpy as np
from scipy.optimize import fsolve


#v=1.717

def answer(num):
	for n in range(1,num+1):
		if n ==1:
			ans = 1.0000
		else: 
			a = lambda v:-v + (n-2)
			b =  lambda v:v + (n-1)
			c =math.factorial(n-1)**2
			d = lambda v:(a*b/c)*(3./4)
			e = answer(n-1)
			ans= lambda v:e*d
	return ans

def funcP(num):
	plist=[]
	for n in range(1,num+1):
		plist.append(answer(n))
	#return plist
	return fsolve(plist, 0.0001)


print (funcP(3))


##########################
##########################
##########################
def problem3(v):
	return 1+((-v)(v+1))*(0.5(1+0.5))+((-v)(-v+1)(v+1)(v+2))/16*(0.5(1+0.5))**2

#print fsolve(problem3, 0.0001)


#fsolve(func, x0, args=(x), fprime=None, full_output=0, col_deriv=0, xtol=1.49012e-08, maxfev=0, band=None, epsfcn=None, factor=100, diag=None)




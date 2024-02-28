# -*- coding: utf-8 -*-
"""
Created on Thu May 10 03:54:02 2018

@author: ibrow
"""

import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

la=[]
TTa=[]
EEa=[]
TEa=[]

lb=[]
TTb=[]
EEb=[]
TEb=[]

lc=[]
TTc=[]
EEc=[]
TEc=[]

ld=[]
TTd=[]
EEd=[]
TEd=[]


#read dat file
for filename in ['NoRcamb_45054732_scalcls.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        la.append(float(line.split()[0])) 
        TTa.append(float(line.split()[1]))
        EEa.append(float(line.split()[2]))
        TEa.append(float(line.split()[3]))

for filename in ['z11camb_32636274_scalcls.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        lb.append(float(line.split()[0])) 
        TTb.append(float(line.split()[1]))
        EEb.append(float(line.split()[2]))
        TEb.append(float(line.split()[3]))
        
for filename in ['z7camb_01609255_scalcls.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        lc.append(float(line.split()[0])) 
        TTc.append(float(line.split()[1]))
        EEc.append(float(line.split()[2]))
        TEc.append(float(line.split()[3]))
   
for filename in ['z20camb_78086006_scalcls.dat']:
    for line in open (filename).readlines():
        if not line.strip() or line[0]=='#':
            continue
        ld.append(float(line.split()[0])) 
        TTd.append(float(line.split()[1]))
        EEd.append(float(line.split()[2]))
        TEd.append(float(line.split()[3]))     
        

fig1=plt.figure()
plt.loglog ((la),(TTa),'g',(la),(EEa),'g',(la),(np.abs(TEa)),'g--')
#plt.plot (np.log(la),np.log(TTa),'g',np.log(la),np.log(EEa),'g',np.log(la),np.log(np.abs(TEa)),'g--')
plt.loglog ((lb),(TTb),'y',(lb),(EEb),'y',(lb),(np.abs(TEb)),'y--')
plt.loglog ((lc),(TTc),'r',(lc),(EEc),'r',(lc),(np.abs(TEc)),'r--')
plt.loglog ((ld),(TTd),'b',(ld),(EEd),'b',(ld),(np.abs(TEd)),'b--')
#plt.xlim(3000,10000)
plt.xlabel('$\ell$',fontsize=16)
plt.ylabel('Amplitude',fontsize=16)    
plt.title('Power spectra from CAMB', fontsize=16)
red = mpatches.Patch(color='red', label='Z=7')
green = mpatches.Patch(color='green', label='No Reionization')
blue = mpatches.Patch(color='blue', label='z=20')
yellow = mpatches.Patch(color='yellow', label='z=11')

plt.legend(handles=[green,red,yellow,blue])

plt.show()

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:07:46 2020

@author: nabendu
"""

import numpy as np
import matplotlib.pyplot as plt

def Euler(t,y):
    return(y/t-(y/t)**2)

t0=1.0    #initial time 
tf=2.0    #final time

h=0.1    #time step

N=int((tf-t0)/h+1)

t=np.linspace(t0,tf,N)

y=np.zeros(N)

y[0]=1.0

for i in range(1,N):
    y[i]=y[i-1]+h*Euler(t[i-1],y[i-1])
    
y_exact=t/(1+np.log(t))            #exact solution
delta=abs(y[i]-y_exact[-1])         #absolute solution
print('absolute error is',delta)
print('relative error',delta/y_exact[-1])       #printing relative error
plt.plot(t,y,'r',label=r'$numerical$')
plt.plot(t,y_exact,'b',label=r'$exact$')
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.legend()
plt.show()

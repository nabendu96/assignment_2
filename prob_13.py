# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 03:14:11 2020

@author: nabendu
"""

#Queston_13
#Solving second-order equation using euler method

import numpy as np
import math
import matplotlib.pyplot as plt

def euler(t,r):
    y=r[0]
    z=r[1]
    f_y=z
    f_z=2*(z/t)-2*(y/t**2)+t*math.log(t)
    return(np.array([f_y,f_z]))

t0=1.0     #start of interval
tf=2.0     #end of interval

h=0.001     #step size

N=int((tf-t0)/h+1)

t=np.linspace(t0,tf,N)

y=np.zeros(N)
y[0]=1.0      #1st initial condition

z=np.zeros(N)
z[0]=0.0       #2nd initial condition

r=np.array([y[0],z[0]])

for i in range(1,N):
    r=r+h*euler(t[i-1],r)
    y[i]=r[0]
    z[i]=r[1]
 
plt.plot(t,y,'r',label='$numerical$')
plt.plot(t,(7/4)*t+(t**3/2)*np.log(t)-(3/4)*t**3,'g',label='$exact$')    #plotting of exact solution
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.legend()
plt.show()

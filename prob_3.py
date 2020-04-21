# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 03:14:11 2020

@author: nabendu
"""

#Queston_3
#Solving second-order equation using rk4

import numpy as np
import math
import matplotlib.pyplot as plt

def rk4(x,r):
    y=r[0]
    z=r[1]
    f_y=z
    f_z=2*z-y+x*math.exp(x)-x
    return(np.array([f_y,f_z]))

x0=0.0      #start of interval 
xf=1.0      #end of interval
N=100       #mesh points

x=np.linspace(x0,xf,N)

h=(xf-x0)/(N-1)

y=np.zeros(N)
y[0]=0.0        #1st initial condition

z=np.zeros(N)
z[0]=0.0        #2nd initial condition

r=np.array([y[0],z[0]])

#rk4
for i in range(1,N):
    k1=h*rk4(x[i-1],r)
    k2=h*rk4(x[i-1]+0.5*h,r+0.5*k1)
    k3=h*rk4(x[i-1]+0.5*h,r+0.5*k2)
    k4=h*rk4(x[i],r+k3)
    r=r+(1/6)*(k1+2*k2+2*k3+k4)
    y[i]=r[0]
    z[i]=r[1]
 
plt.plot(x,y)
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.show()

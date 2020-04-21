# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:30:35 2020

@author: nabendu
"""

#problem_1: Solving ode using euler backward
 
import numpy as np
import math
import matplotlib.pyplot as plt
    
def euler_backward_2(x,y2):
    return(-20*(y2-x)**2+2*x)

#Newton Raphson method to find solution of non-linear equation for the second case
def newton_raphson(x,y2,h):
    accuracy=10**(-12)
    y2prime=0.0
    delta=1.0
    while(abs(delta)>accuracy):
        f=y2prime-y2-h*euler_backward_2(x,y2prime)
        fprime=1+40*h*(y2prime-x)
        delta=f/fprime
        y2prime=y2prime-delta
    return(y2prime)
        
        
x0=0    #start of interval
xf=1    #end of interval
N=100   #no of grid points

x=np.linspace(x0,xf,N)

h=(xf-x0)/(N-1)

y1=np.zeros(N)

y2=np.zeros(N)

y1[0]=math.exp(1)   #initial condition for 1st ode

y2[0]=1/3   #initial condition for 2nd ode

for i in range(1,N):
    y1[i]=y1[i-1]/(1+9*h)
    y2[i]=newton_raphson(x[i],y2[i-1],h)
    
plt.plot(x,y1,'r')
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.text(0.7,2,r'$\frac{dy}{dx}=-9y$',fontsize=20)
plt.show()

plt.plot(x,y2,'c')
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.text(0,1,r'$\frac{dy}{dx}=-20(y-x)^2+2x$',fontsize=20)
plt.show()
    
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:35:00 2020

@author: nabendu
"""

#problem 10
#solution over infinite ranges

import numpy as np
import matplotlib.pyplot as plt

#transformed x' as a function of x and u 
def rk4(u,x):
    return(1/(x**2*(1-u)**2+u**2))

#transforming the variable t into new variable u of finite span
u0=0.0
uf=1.0

N=10**5      #number of mesh points

h=(uf-u0)/N

u=np.arange(u0,uf,h)

#reading the t values from u array
t=np.zeros(N)
t=u/(1-u)

x=np.zeros(N)

x[0]=1.0      #initial condition

#rk4
for i in range(1,N):
    k1=h*rk4(u[i-1],x[i-1])
    k2=h*rk4(u[i-1]+0.5*h,x[i-1]+0.5*k1)
    k3=h*rk4(u[i-1]+0.5*h,x[i-1]+0.5*k2)
    k4=h*rk4(u[i],x[i-1]+k3)
    x[i]=x[i-1]+(1/6)*(k1+2*k2+2*k3+k4)
    
plt.plot(t,x,'b')
plt.xlim(0,100)        #the solution is ploted for a finite span of time
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$x$',fontsize=20)
plt.show()

print('The value of solution at t=3.5*10^6 is approximately',x[-1])
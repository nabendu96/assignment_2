# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:18:02 2020

@author: nabendu
"""

#Queston_11
#Simultaneous ordinary differential equations

import numpy as np
import math
import matplotlib.pyplot as plt

def rk4(t,r):
    u1=r[0]
    u2=r[1]
    u3=r[2]
    f_u1=u1+2*u2-2*u3+math.exp(-t)
    f_u2=u2+u3-2*math.exp(-t)
    f_u3=u1+2*u2+math.exp(-t)
    return(np.array([f_u1,f_u2,f_u3]))

t0=0.0       #start of interval
tf=1.0       #end of interval
N=100

t=np.linspace(t0,tf,N)

h=(tf-t0)/(N-1)

u1=np.zeros(N)
u1[0]=3.0     #1st initial condition

u2=np.zeros(N)
u2[0]=-1.0       #2nd initial condition

u3=np.zeros(N)
u3[0]=1.0         #3rd initial condition

r=np.array([u1[0],u2[0],u3[0]])

#rk4
for i in range(1,N):
    k1=h*rk4(t[i-1],r)
    k2=h*rk4(t[i-1]+0.5*h,r+0.5*k1)
    k3=h*rk4(t[i-1]+0.5*h,r+0.5*k2)
    k4=h*rk4(t[i],r+k3)
    r=r+(1/6)*(k1+2*k2+2*k3+k4)
    u1[i]=r[0]
    u2[i]=r[1]
    u3[i]=r[2]
 
plt.plot(t,u1,'r',label='$u_1$')
plt.plot(t,u2,'b',label='$u_2$')
plt.plot(t,u3,'k',label='$u_3$')
plt.xlabel(r'$t$',fontsize=20)
plt.legend()
plt.show

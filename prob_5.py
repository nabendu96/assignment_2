# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:18:53 2020

@author: nabendu
"""

#problem_5
#Shooting method for solving boundary value problem

import numpy as np
import matplotlib.pyplot as plt

g=10

#boundary conditions
t0=0
x0=0
tf=10
xf=0

N=100       #number of mesh points

t=np.linspace(t0,tf,N)

h=(tf-t0)/(N-1)

target=10**(-10)        #target accuracy for binary search

solutions=[]

def rk4(t,r):
    x=r[0]
    y=r[1]
    fx=y
    fy=-g
    return(np.array([fx,fy]))

#function to solve the equation, calculate the solution arrays and plot the candidate solutions    #rk4
def xarray(v):
    t=np.linspace(t0,tf,N)
    x=np.zeros(N)
    x[0]=0.0
    y=np.zeros(N)
    y[0]=v
    r=np.array([x[0],y[0]])
    for i in range(1,N):
        rHalf_1=r+0.5*h*rk4(t[i-1],r)
        rHalf_2=r+0.5*h*rk4(t[i-1]+0.5*h,rHalf_1)
        r_1=r+h*rk4(t[i-1]+0.5*h,rHalf_2)
        r=r+(1/6)*h*(rk4(t[i-1],r)+2*rk4(t[i-1]+0.5*h,rHalf_1))+(1/6)*h*(2*rk4(t[i-1]+0.5*h,rHalf_2)+rk4(t[i],r_1))
        x[i]=r[0]
        y[i]=r[1]
    plt.plot(t,x,'lightgray')
    return(x)
    
#main program perform a binary search    
#initially assumed velocities
v1=0.01
v2=100
x1=xarray(v1)
x2=xarray(v2)
solutions.append(x1)
solutions.append(x2)
h1=x1[-1]
h2=x2[-1]

count=2

while(abs(h2-h1)>target):
    vp=(v1+v2)/2
    xp=xarray(vp)
    solutions.append(xp)
    hp=xp[-1]
    count=count+1
    if(h1*hp>0):
        v1=vp
        h1=hp
    else:
        v2=vp
        h2=hp
        
v=(v1+v2)/2
x=xarray(v)
solutions.append(x)
h=x[-1]
count=count+1
print('initial velocity',v)

numeric_solution=np.zeros(N)

for i in range(N):
    numeric_solution[i]=solutions[-1][i]
plt.plot(t,numeric_solution,'c',label=r'$numerical$')
plt.plot(t,-g*t**2/2+g*tf*t/2,'r',label=r'$exact$')    #plotting exact solution 
plt.axhline(0,color='k')
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$x$',fontsize=20)
plt.legend()
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:20:31 2020

@author: nabendu
"""

#question_6
#solving boundary value problem using relaxation method

import numpy as np
import matplotlib.pyplot as plt

g=10

#boundary conditions
t0=0
x0=0
tf=10
xf=0

N=100      #number of mesh points

t=np.linspace(t0,tf,N)

h=(tf-t0)/(N-1)

target=0.001      #target accuracy 

x=np.zeros(N)
x[0]=x0
x[-1]=xf

solutions=[]

xprime=np.zeros(N)

count=0

#finding solution using relaxation
for m in range(1000000):
    for i in range(N):
        if(i==0 or i==N-1):
            xprime[i]=x[i]
        else:
            xprime[i]=(x[i+1]+x[i-1]+g*h**2)/2
    delta=max(abs(x-xprime))
    for j in range(N):
        x[j]=xprime[j]
    solutions.append(np.array(x))
    count=count+1
    if(delta<target):       #checking accuracy condition
        break

candidate_solution=np.zeros(N)

n1=0

#ploting the candidate solutions
for i in range(5):
    n1=n1+int(count/6)
    for j in range(N):
        candidate_solution[j]=solutions[n1][j]
    plt.plot(t,candidate_solution,'lightgrey')
    
plt.plot(t,x,'r',label=r'$numerical$')             #numerical solution
plt.plot(t,-g*t**2/2+g*tf*t/2,'c',label=r'$exact$')     #exact solution
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$x$',fontsize=20)
plt.legend()
plt.show()

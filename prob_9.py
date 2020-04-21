# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:00:01 2020

@author: nabendu
"""

#problem_9
#adaptive step-size control

import numpy as np
import matplotlib.pyplot as plt

def rk4(t,y):
    return((y**2+y)/t)
    
def f(t,y,h):    
    yHalf_1=y+0.5*h*rk4(t,y)
    yHalf_2=y+0.5*h*rk4(t+0.5*h,yHalf_1)
    y_1=y+h*rk4(t+0.5*h,yHalf_2)
    return(y+(1/6)*h*(rk4(t,y)+2*rk4(t+0.5*h,yHalf_1))+(1/6)*h*(2*rk4(t+0.5*h,yHalf_2)+rk4(t,y_1)))
    
delta=10**(-4)/2          #target accuracy

h=0.1        #initial guess of h

tpoints=[]

ypoints=[]

t=1.0      #starting of interval

tf=3.0       #end of interval

y=-2.0        #initial condition

tpoints.append(t)
ypoints.append(y)  
    
while(t<tf):
    y_1=f(t,y,h)
    y_2=f(t+h,y_1,h)
    y_3=f(t,y,2*h)
    rho=(30*h*delta)/(abs(y_2-y_3))
    if(rho>=1):        #condition when accuracy better than required
        ypoints.append(y_1)
        ypoints.append(y_2)
        tpoints.append(t+h)
        tpoints.append(t+2*h)
        t=t+2*h
        h=h*rho**(1/4)
    else:            #for worse accuracy and repeating the calculation again
        h=h*rho**(1/4)
        y_1=f(t,y,h)
        y_2=f(t+h,y_1,h)
        ypoints.append(y_1)
        ypoints.append(y_2)
        tpoints.append(t+h)
        tpoints.append(t+2*h)
        t=t+2*h
    y=y_2
        
T=np.array(tpoints)
Y=np.array(ypoints)

plt.plot(T,Y,'r.')
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
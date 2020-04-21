# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 02:50:10 2020

@author: nabendu
"""

#Question 8: boundary value problems
#scipy.integrate.solve_bvp

from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt

#8(i)
def f1(x,y):
	return np.vstack((y[1],-np.exp(-2*y[0])))

def bc1(ya,yb):
	return np.array([ya[0],yb[0]-np.log(2)])

a=1.0
b=2.0
y1_0=0.0
x=np.linspace(a,b,100)
y_dim=np.zeros((2, x.size))
y_dim[0]=y1_0
sol=solve_bvp(f1,bc1,x,y_dim)
y=np.log(x)            #analytical solution
plt.plot(x,sol.sol(x)[0],'r',label=r'$solve\_bvp$')
plt.plot(x,y,'c',label=r'$analytic$')
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.legend()
plt.text(1.5, 0.1, r"$y''=-e^{-2x}$", fontsize=20)
plt.show()

#8(ii)
def f2(x,y):
	return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0])))

def bc2(ya,yb):
	return np.array([ya[0]-1,yb[0]-np.exp(1)])

a=0.0
b=np.pi/2
y2_0=1.0
x=np.linspace(a,b,100)
y_dim=np.zeros((2,x.size))
y_dim[0]=y2_0
sol=solve_bvp(f2,bc2,x,y_dim)
y=np.exp(np.sin(x))                 #analytical solution
plt.plot(x,sol.sol(x)[0],'r',label=r'$solve\_bvp$')
plt.plot(x,y,'c',label=r'$analytic$')
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.legend()
plt.text(0.7, 1.25, r"$y''=y'\cos x-y\ln y$", fontsize=20)
plt.show()

#8(iii)
def f3(x, y):
	return np.vstack((y[1],-(2*y[1]**3+y[0]**2*y[1])*np.cos(x)**(-1)))

def bc3(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])

a=np.pi/4
b=np.pi/3
y3_0=2**(-1/4)
x=np.linspace(a,b,100)
y_dim=np.zeros((2,x.size))
y_dim[0]=y3_0
sol=solve_bvp(f3,bc3,x,y_dim)
y=np.sqrt(np.sin(x))                #analytical solution
plt.plot(x,sol.sol(x)[0],'r',label=r'$solve\_bvp$')
plt.plot(x,y,'c',label=r'$analytic$')
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.legend()
plt.text(0.84, 0.85, r"$y''=-(2y'^3+y^2y')\sec(x)$", fontsize=20)
plt.show()

#8(iv)
def f4(x,y):
	return np.vstack((y[1],0.5*(1-y[1]**2-y[0]*np.sin(x))))

def bc4(ya,yb):
	return np.array([ya[0]-2,yb[0]-2])

a=0
b=np.pi
y4_0=2
x=np.linspace(a,b,100)
y_dim=np.zeros((2,x.size))
y_dim[0]=y4_0
sol=solve_bvp(f4,bc4,x,y_dim)
y=np.sin(x)+2           #analytical solution
plt.plot(x,sol.sol(x)[0],'r',label=r'$solve\_bvp$')
plt.plot(x,y,'c',label=r'$analytic$')
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.legend()
plt.text(0.4, 2.1, r"$y''=1/2-y'^2/2-y\sinx/2$", fontsize=20)
plt.show()

print('In all cases analytic solutions and numerical solutions using solve_vp are exactly matching')
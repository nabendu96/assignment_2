# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:22:12 2020

@author: nabendu
"""

#question 7
#scipy.integrate.solve_ivp

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#7(i)
def f1(t,y):
	return(t*np.exp(3*t)-2*y)
    
sol=solve_ivp(lambda t, y:f1(t,y), [0.0, 1.0], [0.0], t_eval=np.linspace(0.0,1.0,100))
t1=np.linspace(0.0,1.0,100)
y1=(5*t1-1)*np.exp(3*t1)/25+np.exp(-2*t1)/25    #analytic solution
plt.plot(sol.t,sol.y[0],'b',label=r'$solve\_ivp$')           #plot of solution using solve_ivp
plt.plot(t1,y1,'r',label=r'$analytical$')
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.text(0,1,r'$\dot{y}=te^{3t}-2y$',fontsize=20)
plt.legend()
plt.show()

#7(ii)
def f2(t,y):
	return(1-(t-y)**2)
    
sol=solve_ivp(lambda t, y:f2(t,y), [2.0, 3.0], [1.0], t_eval=np.linspace(2.0,3.0,100))
t2=np.linspace(2.0,3.0,100)
y2=(1-3*t2+t2**2)/(-3+t2)                    #analytic solution
plt.plot(sol.t,sol.y[0],'b',label=r'$solve\_ivp$')                   #plot of solution using solve_ivp
plt.plot(t2,y2,'r',label=r'$analytical$')
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.text(2,-60,r'$\dot{y}=1-(t-y)^2$',fontsize=20)
plt.legend()
plt.show()

#7(iii)
def f3(t,y):
	return(1+y/t)
    
sol=solve_ivp(lambda t, y:f3(t,y), [1.0, 2.0], [2.0], t_eval=np.linspace(1.0,2.0,100))
t3=np.linspace(1.0,2.0,100)
y3=t3*(2+np.log(t3))                  #analytic solution
plt.plot(sol.t,sol.y[0],'b',label=r'$solve\_ivp$')          #plot of solution using solve_ivp
plt.plot(t3,y3,'r',label=r'$analytical$')
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.text(1.6,2.5,r'$\dot{y}=1+y/t$',fontsize=20)
plt.legend()
plt.show()

#7(iv)
def f4(t,y):
	return(np.cos(2*t)+np.sin(3*t))
    
sol=solve_ivp(lambda t, y:f4(t,y), [0.0, 1.0], [1.0], t_eval=np.linspace(0.0,1.0,100))
t4=np.linspace(0.0,1.0,100)
y4=np.sin(2*t4)/2-np.cos(3*t4)/3+4/3              #analytic solution
plt.plot(sol.t,sol.y[0],'b',label=r'$solve\_ivp$')                  #plot of solution using solve_ivp
plt.plot(t4,y4,'r',label=r'$analytical$')
plt.xlabel(r'$t$',fontsize=20)
plt.ylabel(r'$y$',fontsize=20)
plt.text(0.4,1.2,r'$\dot{y}=\cos(2t)+\sin(3t)$',fontsize=20)
plt.legend()
plt.show()

print('All the four solutions are exactly matching with analytic solution')

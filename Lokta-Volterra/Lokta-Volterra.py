# Lokta-Volterra model
# from scipy tutorial

# du/dt =  a*u -   b*u*v
# dv/dt = -c*v + d*b*u*v
# where:
# u: number of preys (for example, rabbits)
# v: number of predators (for example, foxes)

# X = [u,v] to track the population of predator-prey over time

from numpy import *
from scipy import integrate
import pylab as p

# Define parameters defining the behavior of the population
# Case: fox is predator, rabbit is prey
a = 1.      # a is the natural growing rate of rabbits, when there's no fox
b = 0.1     # b is the natural dying rate of rabbits, due to predation
c = 1.5     # c is the natural dying rate of fox, when there's no rabbit
d = 0.75    # d is the factor describing how many caught rabbits let create a new fox

def dX_dt(X, t=0):
    """Return the growth rate of predator and prey population"""
    return array([a*X[0] - b*X[1]*X[0],
                  -c*X[1] + d*b*X[1]*X[0]])

t = linspace(0, 15, 1000)   # time until 1000 days, with 15 days interval
X0 = array([10, 5])         # initial population (rabbit, fox)
X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
infodict['message']         # integration successful

rabbits, foxes = X.T
f1 = p.figure()
p.plot(t, rabbits, 'r-', label='Rabbits')
p.plot(t, foxes, 'b-', label='Foxes')
p.grid()
p.legend(loc='best')
p.xlabel('time')
p.ylabel('population')
p.title('Evolution of foxes and rabbits population')
f1.savefig('rabbits_foxes.png')
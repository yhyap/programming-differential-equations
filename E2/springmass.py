# Implementing oscillating spring-mass system

# 2nd order ODE for spring mass system
# m*d2u/dt2 + beta*du/dt + k*u = F(t)

# with the initial condition
# u(0) = U0
# du/dt(0) = 0

# This 2nd order ODE can be written as two 1st order ODE
# Let u[0] = u
# Let u[1] = du/dt
    # as two functions:
    # du[0]/dt = u[1]
    # du[1]/dt = 1/m*(F(t) - beta*u[1] - k*u[0])
    
#def f(u, t):
#    return np.array([u[1], 1./m*(F(t) - beta*u[1] - k*u[0])])
    
    
    
# For application: d2u/dt2 + u = 0
# with condition: u(0) = 0
# du/du(0) = 1
    
#from NumericalMethod import ForwardEuler as fe
from ODESolver import ForwardEuler as fe
from ODESolver import RungeKutta4 as rk4
from ODESolver import BackwardEuler as be
import numpy as np
    
def f(u, t):
    return [u[1], -u[0]]
    
U0 = [0, 1]                 # Initial condition for both u(0) and du/dt(0)

# Call the type of ODESolver class and assign initial condition
#method = fe(f)                      # use forward euler method
#method = rk4(f)                     # use 4th order Runge-Kutta method
method = be(f)                      # use Backward Euler method
method.set_initial_condition(U0)

# Assign T and n
T = 12                      # final time
n = 100                     # no. of steps
t = np.linspace(0, T, n+1)  # time steps from 0 to T in n+1 steps
u, t = method.solve(t)      # solve
u0 = u[:, 0]                # only get the first term in all arrays
u1 = u[:, 1]                # only get the second term in all array


print u
print t



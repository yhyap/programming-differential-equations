# Programming of scalar ODE
# Some examples:
    # exponential growth of money or population
    # logistic growth of population under limited resources
    # Lotka-Volterra competition model
    # Radioactive decay of a substance
    # Body falling in a fluid
    # Newton's Law of Cooling

from NumericalMethods import ForwardEuler as FE
import numpy as np

# Example function f = du/dt = u
def _f1(u, t):
    return u

# Testing with different numerical methods
def _verify_f1_ForwardEuler():
    U0 = 3
    method = FE(_f1)
    method.set_initial_condition(U0)
    t = [0, 0.4, 1, 1.2]
    u1, t1 = method.solve(t)
    
    # Continue with new time interval
    method.set_initial_condition(u1[-1])    # the last solution
    t = [1.2, 1.4, 1.5]
    u2, t2 = method.solve(t)
    u = np.concatenate((u1, u2))
    t = np.concatenate((t1, t2))
    #u_exact = u_solution_f1(t)
    print 'time_value: ', t
    print 'Numerical: ', u
    #print 'Exact: ', u_exact
    
_verify_f1_ForwardEuler()

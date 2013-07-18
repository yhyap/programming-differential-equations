from NumericalMethods import ForwardEuler as FE
import numpy as np

class Logistic:
    """Problem class for a logistic ODE"""
    def __init__(self, alpha, R, U0):
        self.alpha, self.R, self.U0 = alpha, float(R), U0
        
    def __call__(self, u, t):
        """Return f(u, t) for the logistic ODE"""
        return self.alpha*u*(1-u/self.R)
        
    def __str__(self):
        """Return ODE and initial condition"""
        return "u(t) =%g*u(1-u/%g) \nu(0)=%g" % (self.alpha, self.R, self.U0)
        

def logistic():
    problem = Logistic(alpha=0.2, R=1, U0=0.1)
    T = 40
    method = FE(problem)
    method.set_initial_condition(problem.U0)
    t = np.linspace(0, T, 401)  # 400 intervals in [0, T]
    u, t = method.solve(t)
    print "Solution: ", u
    
logistic()
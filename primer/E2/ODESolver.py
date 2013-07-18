
import numpy as np
from Derivative import Derivative
from Newton import Newton


class ODESolver:
    """
    A superclass for solving ODE(s)
    
        du/dt = f(u,t)
    
    This superclass can be inherited to create other subclass
    such as Forward Euler, Backward Euler etc.
    
    Class attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(u,t)
    """
    
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = lambda u, t: np.asarray(f(u, t), float)   
        # lambda is anonymous function construct
        # here f is transformed into an array
        
    def set_initial_condition(self, U0):
        if isinstance(U0, (float, int)):    # Scalar ODE
            self.neq = 1                    # number of equation
            U0 = float(U0)
        else:                               # System of ODE
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0
        
    def solve(self, time_points, terminate=None):
        """Compute u for t values in time points list"""
        if terminate is None:
            terminate = lambda u, t, step_no: False
            
        self.t = np.asarray(time_points)
        n = self.t.size
        if self.neq == 1:                   # if scalar ODE
            self.u = np.zeros(n)
        else:                               # systems of ODEs
            self.u = np.zeros((n, self.neq))
        
        # Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0
        
        # Time loop
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break                       # terminate loop over k
        return self.u, self.t
        
    def advance(self):
        """Advance the solution one step ahead"""
        raise NotImplementedError
        

class ForwardEuler(ODESolver):
    """Forward Euler advancing algorithm"""
    def advance(self):
        u, f, t, k = self.u, self.f, self.t, self.k
        dt = t[k+1] - t[k]
        unew = u[k] + dt*f(u[k], t[k])
        return unew
        

class RungeKutta4(ODESolver):
    """4th-order Runge-Kutta advancing algorithm"""
    def advance(self):
        u, f, t, k = self.u, self.f, self.t, self.k
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + dt2)
        K3 = dt*f(u[k] + 0.5*K2, t[k] + dt2)
        K4 = dt*f(u[k] + K3, t[k] + dt)
        unew = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return unew
        

class BackwardEuler(ODESolver):
    """Backward Euler advancing algorithm"""
    def __init__(self, f):
        ODESolver.__init__(self, f)
        # Make a sample call to check that f is a scalar function
        try:
            u = np.array([1]); t=1
            value = f(u, t)
        except IndexError:      # index out of bounds for u
            raise ValueError('f(u,t) must return float/int')
        
        
    def advance(self):
        u, f, t, k = self.u, self.f, self.t, self.k
        dt = t[k+1] - t[k]        
        
        def F(w):
            # From BE where: u[k+1] = u[k] + dt*f(u[k+1], t[k+1])
            # Create a F(w) = ... move all terms in eqn above to left hand side
            return w - dt*f(w, t[k+1]) - u[k]   # where w = u[k+1], 
            # returns a vector of functions, only works if w is a vector
            
        dFdw = Derivative(F)
        w_start = u[k] + dt*f(u[k], t[k])       # Estimate using Forward Euler
        unew, n, F_value = Newton(F, w_start, dFdw, N=30)
        if k == 0:
            self.Newton_iter = []
        self.Newton_iter.append(n)
        if n >= 30:
            print "Newton's method failed to converge at t=%g "\
                    "(%d iterations)" % (t, n)
        return unew
            
    

            
        
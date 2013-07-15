import numpy as np

#def ForwardEuler(f, U0, Tf, n):
    #"""Solve u'=f(u, t), u(0)=U0, with n steps until t=Tf"""
    ## Set all initial solution as zeros
    #t = np.zeros(n+1)
    #u = np.zeros(n+1)
    #u[0] = U0
    #t[0] = 0
    #dt = Tf/float(n)
    #for k in range(n):
        #t[k+1] = t[k]+dt
        #u[k+1] = u[k]+dt*f(u[k], t[k])
    #return u, t     # returns solution at different time steps


class ForwardEuler:
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = f                             # function, initial condition, final time, no. of steps
        
    def set_initial_condition(self, U0):
        self.U0 = float(U0)
        
    def solve(self, time_points):
        """Compute u for t values in time_points list"""
        self.t = np.asarray(time_points)       # create it as array
        self.u = np.zeros(len(time_points))    # array - zero for all time steps
        # Assume self.t[0] corresponds to self.U0
        self.u[0] = self.U0                    # inlet condition
        
        for k in range(len(self.t)-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t
    
    def advance(self):
        """Advance the solution one time step"""
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        unew = u[k] + dt*f(u[k], t[k])
        return unew
        
        
    
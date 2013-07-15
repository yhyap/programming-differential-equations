# Model the motion of oscillating system of spring with a box
    # F = ma
    # ma = -mg + kS + beta*dS/dt
    # m(d2w/dt2 - d2S/dt2) = -mg + kS + beta*dS/dt)
    # Moving unknowns to LHS
    # m(d2S/dt2 + beta*dS/dt + kS) = m(d2w/dt2 + g)
    # v(t) = dw/dt - dS/dt

# Above equations can be modeled by two ODE
    # just like in springmass.py
    # m*d2u/dt2 + beta*du/dt + k*u = F(t)
    # where u here is S above
# make d2u/dt2 as subject:
    # d2u/dt2 = 1/m(F(t) - beta*du/dt - k*u)

# The 2nd order ODE can be written as two 1st order ODE and for our system:
# Let u[0] = u
# Let u[1] = du/dt
    # as two functions:
    # du[0]/dt = u[1]
    # du[1]/dt = 1/m*(m*(d2w/dt2 + g) - beta*u[1] - k*u[0])
    #           = d2w/dt2 + g - 1/m*beta*u[1] - 1/m*ku[0]


import ODESolver

class OscSystem:
    def __init__(self, m, beta, k, g, w):
        self.m = float(m)          # mass of box
        self.beta = float(beta)    # damping constant, against and proportional to the velocity of stretch
        self.k = float(k)          # spring constant
        self.g = float(g)          # gravitational acceleration
        self.w = w                 # position like x,y,z
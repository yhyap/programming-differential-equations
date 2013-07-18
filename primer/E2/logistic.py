# Logistic Equation

# dp/dt = alpha*p * (1 - p/R)
# Logistic function: p(t) = 1/(1+exp(-t))
# alpha and R can be removed
# It becomes dp/dt = p(1-p), p(0) = p0/R

import numpy as np
import ODESolver
import matplotlib.pyplot as plt


# Parameter
p0 = 0.05       # starting population

# Time points
dtau = 0.05
T = 10
n = int(round(T/dtau))
t_points = np.linspace(0, T, n+1)

# Calling Runge-Kutta solver
method = ODESolver.RungeKutta4(lambda p, tau: p*(1-p))
method.set_initial_condition(p0)
p, tau = method.solve(t_points)


print p

f1 = plt.figure()
plt.plot(tau, p, title='logistic equation')
# PROBLEM 2
# 
# This is a model without any immunity.
# Set the step size h to 10, notice 
# what happens, and then reset it to 0.5.
# Afterwards, convert the below si_model 
# function from the Forward Euler Method 
# to the Trapezoidal Rule.
# To do this, note that s + i is constant. 
# Solve the equation for i, and then compute s 
# from that.
# After you're done, set the step size h 
# to 10 again and see what happens. Submit 
# the problem with that step size.

import numpy
import math
import matplotlib.pyplot

h = 0.5 # days
end_time = 60. # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def si_model():
    transmission_coeff = 5e-9 # 1 / (day * person)
    infectious_time = 5. # days

    s = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e5
    i[0] = 1e5
    N = s[0] + i[0]     # total population remains constant

    for step in range(num_steps):
        # Solve using the Trapezoidal Rule
        # In the derivation, a = transmission coeff, b = 1 / infectious time
        p = (2. / h - transmission_coeff * N + 1.0 / infectious_time) / transmission_coeff
        q = (-2. * i[step] / h - transmission_coeff * i[step] * N + transmission_coeff * i[step]**2 + 1. / infectious_time * i[step]) / transmission_coeff 
        i[step + 1] = -p/2.0 + math.sqrt(p**2.0/4.0 - q)
        s[step + 1] = N - i[step+1]


    return s, i

s, i = si_model()
    

def plot_me():
    s_plot = matplotlib.pyplot.plot(times, s, label = 'S')
    i_plot = matplotlib.pyplot.plot(times, i, label = 'I')
    matplotlib.pyplot.legend(('S', 'I'), loc = 'upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Number of persons')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    matplotlib.pyplot.show()
plot_me()


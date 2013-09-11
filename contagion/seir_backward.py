# QUIZ
# 
# The function backward_euler below currently implements 
# the Forward Euler Method. Modify it to implement the 
# Backward Euler Method. When you're done, set the step 
# size h to 5. and see what happens!

import matplotlib.pyplot
import math
import numpy

h = 5. # days
transmission_coeff = 5e-9 # 1 / day person
latency_time = 1. # days
infectious_time = 5. # days

end_time = 60. # days
num_steps = int(end_time / h)

times = h * numpy.array(range(num_steps + 1))

def backward_euler():

    s = numpy.zeros(num_steps + 1)
    e = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)
    r = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e6 - 1e5
    e[0] = 0.
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        # Forward Euler Method code
        #s2e = h * transmission_coeff * s[step] * i[step]
        #e2i = h / latency_time * e[step]
        #i2r = h / infectious_time * i[step]

        ##### Tip: Start going from implicit to explict by treating one equation at a time and checking if the result is still ok. 
        #####      Start with the equation for r, then move to s, i, and e. Once you're done, change the step size h to 5.

        #######SPOILER ALERT: This is the result for e[step + 1] from the Backward Euler method
        # You may simply remove the comment signs to use it.
        # Given enough practice in algebra, however, you may want to spend half an hour and derive this yourself.
        # In essence, the derivation boils down to solving a quadratic equation.
        # Start by expressing e[step + 1] + s[step + 1] with the help of e[step] and s[step].    
        p = ((1.0 + h / infectious_time) / (h * transmission_coeff) + i[step]) / (h / latency_time) - (s[step] + e[step]) / (1.0 + h / latency_time) 
        q = -((1.0 + h / infectious_time) / (h * transmission_coeff) * e[step] + (s[step] + e[step]) * i[step]) / ((1.0 + h / latency_time) * (h / latency_time))
        e[step + 1] = -0.5 * p + math.sqrt(0.25 * p * p - q)
        i[step + 1] = (i[step] + h / latency_time * e[step + 1]) / (1.0 + h / infectious_time)
        s[step + 1] = s[step] / (1.0 + h * transmission_coeff * i[step+1])
        r[step + 1] = r[step] + h / infectious_time * i[step+1]


    return s, e, i, r

s, e, i, r = backward_euler()


def plot_me():
    s_plot = matplotlib.pyplot.plot(times, s, label = 'S')
    e_plot = matplotlib.pyplot.plot(times, e, label = 'E')
    i_plot = matplotlib.pyplot.plot(times, i, label = 'I')
    r_plot = matplotlib.pyplot.plot(times, r, label = 'R')
    matplotlib.pyplot.legend(('S', 'E', 'I', 'R'), loc = 'upper right')
    
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Number of persons')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    matplotlib.pyplot.show()

plot_me()



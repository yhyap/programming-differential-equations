# SEIR model

# QUIZ
# 
# In the seir_model function below, 
# solve the SEIR model using the 
# Forward Euler Method.

import matplotlib.pyplot
import numpy

h = 0.5 # days
transmission_coeff = 5e-9 # 1 / day person
latency_time = 1. # days
infectious_time = 5. # days

end_time = 60.0 # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def seir_model():

    s = numpy.zeros(num_steps + 1)
    e = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)
    r = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e6 - 1e5
    e[0] = 0.
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        s[step+1] = s[step] - h*transmission_coeff*i[step]*s[step]
        e[step+1] = e[step] + h*(transmission_coeff*i[step]*s[step] - 1./latency_time*e[step])
        i[step+1] = i[step] + h*(1./latency_time*e[step] - 1./infectious_time*i[step])
        r[step+1] = r[step] + h*(1./infectious_time*i[step])
        
    return s, e, i, r

s, e, i, r = seir_model()


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



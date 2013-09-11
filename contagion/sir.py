# PROBLEM 1
# 
# Include waning immunity in the SIR model, so 
# that people can eventually become susceptible 
# again. Define the time constant waning_time 
# such that eventually there are twice as many 
# recovered people as there are infected people.

import matplotlib.pyplot
import numpy

h = 0.5 # days
end_time = 60. # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def waning():
    transmission_coeff = 5e-9 # 1 / (day * person)
    infectious_time = 5. # days

    waning_time = infectious_time * 2.0

    s = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)
    r = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e6 - 1e5
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        s2i = h * transmission_coeff * s[step] * i[step]
        i2r = h / infectious_time * i[step]
        r2s = h / waning_time * r[step]
        ### Modify the below code
        s[step + 1] = s[step] - s2i + r2s
        i[step + 1] = i[step] + s2i - i2r
        r[step + 1] = r[step] + i2r - r2s
        ### End code to modify

    return s, i, r

s, i, r = waning()


def plot_me():
    s_plot = matplotlib.pyplot.plot(times, s, label = 'S')
    i_plot = matplotlib.pyplot.plot(times, i, label = 'I')
    r_plot = matplotlib.pyplot.plot(times, r, label = 'R')
    matplotlib.pyplot.legend(('S', 'I', 'R'), loc = 'upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Number of persons')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    matplotlib.pyplot.show()
plot_me()


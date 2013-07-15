import math
import numpy
from matplotlib import pyplot

moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    for i in range(num_steps + 1):
        angle = 2. * math.pi * i / num_steps
        x[i, 0] = moon_distance*math.cos(angle)
        x[i, 1] = moon_distance*math.sin(angle)

    return x

x = orbit()


# test
def plot_me():
    pyplot.axis('equal')
    pyplot.plot(x[:, 0], x[:, 1])
    axes = pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    pyplot.show()
plot_me()


# QUIZ
# 
# Fill in the for loop below to set 
# the x, y1, and y2 arrays to the 
# following values:
#
# - The x array should contain 
#   num_points many points evenly 
#   spaced between 0 and 2*pi.
#   0 and 2*pi should be included.
#
# - The y1 array should contain 
#   the corresponding sine values 
#   of the values in the x array.
#
# - The y2 array should contain 
#   the corresponding cosine values
#   of the values in the x array.

import math
from matplotlib import pyplot
import numpy


def sin_cos():
    num_points = 50

    x = numpy.zeros(num_points)
    sin_x = numpy.zeros(num_points)
    cos_x = numpy.zeros(num_points)

    for i in range(num_points):
        x[i] = 2*math.pi*i/(num_points - 1.)
        sin_x[i] = math.sin(x[i])
        cos_x[i] = math.cos(x[i])
    return x, sin_x, cos_x

x, sin_x, cos_x = sin_cos()

# These lines call the matplotlib package
# to plot the values you input on a graph.
#@show_plot
def plot_me():
    pyplot.plot(x, sin_x)
    pyplot.plot(x, cos_x)
    pyplot.show()
plot_me()


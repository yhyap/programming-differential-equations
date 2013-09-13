import math
import numpy
from matplotlib import pyplot

moon_distance = 384e6                   # m
h = 0.1                                 # s
g = 9.81                                # m / s2
initial_speed = 20.                     # m / s
acceleration = numpy.array([0., -g])    # acceleration in horizontal, vertical


# simple orbit
def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    for i in range(num_steps + 1):
        angle = 2. * math.pi * i / num_steps
        x[i, 0] = moon_distance*math.cos(angle)
        x[i, 1] = moon_distance*math.sin(angle)

    return x


def trajectory():
    angles = numpy.linspace(20., 70., 6)
    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        angle_rad = math.pi/180. * angle
        x[0,0] = 0
        x[0,1] = 0
        v[0,0] = initial_speed*math.cos(angle_rad)
        v[0,1] = initial_speed*math.sin(angle_rad)
        for i in range(num_steps):
            x[i+1] = x[i] + h*v[i]
            v[i+1] = v[i] + h*acceleration

        pyplot.plot(x[:, 0], x[:, 1])
    pyplot.axis('equal')
    axes = pyplot.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    pyplot.show()
    return x, v

trajectory()

# test orbit
def plot_me():
    pyplot.axis('equal')
    pyplot.plot(x[:, 0], x[:, 1])
    axes = pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    pyplot.show()
plot_me()

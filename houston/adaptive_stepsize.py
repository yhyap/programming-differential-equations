import numpy
from matplotlib import pyplot
import math

def acceleration(spaceship_position):
    earth_mass = 5.97e24 # kg
    gravitational_constant = 6.67e-11 # N m2 / kg2
    vector_to_earth = - spaceship_position # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth
 
# orbit constructed by adaptive step size 
def orbit2():
    total_time = 12500. # s
    x = numpy.zeros(2) # m
    v = numpy.zeros(2) # m / s
    x[0] = 15e6
    x[1] = 1e6    
    v[0] = 2e3
    v[1] = 4e3
    pyplot.scatter(x[0], x[1], s = 4)

    current_time = 0. # s
    h = 100. # s
    h_new = h # s, will store the adaptive step size of the next step
    tolerance = 5e5 # m

    while current_time < total_time:
        acceleration0 = acceleration(x)    
        xE = x + h * v
        vE = v + h * acceleration0
        xH = x + h * 0.5 * (v + vE)
        vH = v + h * 0.5 * (acceleration0 + acceleration(xE))
        x = xH
        v = vH
        
        error = numpy.linalg.norm(xH-xE) + total_time*numpy.linalg.norm(vH-vE)
        h_new = h * math.sqrt(tolerance/(error + math.e**-50))
        # h_new = min(1800., max(0.1, h_new))
        
        pyplot.scatter(x[0], x[1], s = 1)
        current_time += h
        h = h_new
    pyplot.axis('equal')
    pyplot.scatter(0., 0.) 
    axes = pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    pyplot.show()
    return x, v

x, v = orbit2()


# Determine the error (global truncation error)

# Compute the trajectory of the spacecraft 
# starting from a point a distance r from 
# the origin with a velocity of magnitude 
# equal to the speed. 

# Use both the Forward Euler Method and Heun's Method 

# Return the distance between the final 
# and the initial position in the variable 
# error.

import math
import numpy
import matplotlib.pyplot

# These are used to keep track of the data we want to plot
h_array = []                                    # time array
euler_error_array = []                          # error array using Euler's
heuns_error_array = []                          # error array using Heun's

total_time = 24. * 3600.                        # s
g = 9.81                                        # m / s2
earth_mass = 5.97e24                            # kg
gravitational_constant = 6.67e-11               # N m2 / kg2
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.)
speed = 2.0 * math.pi * radius / total_time     # 2*pi*r/T

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position      # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def calculate_error(num_steps):
    h = total_time / num_steps
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])
    
    x[0,0] = radius                             # initial position at [R, 0]
    v[0,1] = speed                              # initial speed with [0, speed]
    
    # Forward Euler method
    for i in range(num_steps):
        x[i+1] = x[i] + h*v[i]
        v[i+1] = v[i] + h*acceleration(x[i])    # acceleration at specific position
    
    error = numpy.linalg.norm(x[-1] - x[0])     # difference between final position and initial
    h_array.append(h)
    euler_error_array.append(error)
 
    # Heun's method   
    for step in range(num_steps):
        init_acceleration = acceleration(x[step])   # store the init_acc from euler's
        xE = x[step] + h * v[step]                  # euler's
        vE = v[step] + h * acceleration(x[step])    # euler's
        x[step + 1] = x[step] + h/2.0 * (v[step] + vE)
        v[step + 1] = v[step] + h/2.0 * (init_acceleration + acceleration(xE))

    error = numpy.linalg.norm(x[-1] - x[0])
    heuns_error_array.append(error)    
    
    return x,v,error
    
h_array=[]
euler_error_array=[]
for num_steps in [50, 200, 500, 1000, 2000, 5000, 10000]:
    x, v, error = calculate_error(num_steps)


def plot_me():
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Step size in s')
    axes.set_ylabel('Error in m')
    matplotlib.pyplot.scatter(h_array, euler_error_array, c = 'g')
    matplotlib.pyplot.scatter(h_array, heuns_error_array, c = 'r')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    matplotlib.pyplot.show()
plot_me()

# Will show that the smaller the step size, the smaller the error
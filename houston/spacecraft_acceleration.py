
# Modify the acceleration function so that it returns 
# the acceleration vector of the spacecraft.

# F = ma(spacecraft) = G*m(earth)*m(spacecraft)/r^2 * vector_to_earth
#                       + G*m(moon)*m(spacecraft)/r^2 * vector_to_moon
# vector = position/distance, therefore

# numpy.linalg.norm function
# -computes the length of the vector, and 
# it should be the only outside function you need to 
# use in your answer.

import numpy

earth_mass = 5.97e24 # kg
moon_mass = 7.35e22 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

# The origin, or (0,0), is at the center of the earth 
# in this example, so it doesn't make any sense to 
# set either the moon_position or spaceship_position
# equal to (0,0). Depending on your solution, doing this
# may throw an error!  Please note that moon_position and 
# spaceship_position are both numpy arrays, and the 
# returned value should also be a numpy array.

def acceleration(moon_position, spaceship_position):
    vector_to_moon = moon_position - spaceship_position
    vector_to_earth = -spaceship_position
    return gravitational_constant * (earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth
                                     + moon_mass / numpy.linalg.norm(vector_to_moon)**3 * vector_to_moon)

# test case
m_p = numpy.array([[4e12], [0.0]])    # moon position
s_p = numpy.array([[6.378e6], [0.0]])   # spaceship position       
print acceleration(m_p, s_p)            # should return about 10m/s2 in -x direction
# QUIZ
# 
# Modify the logistic_growth function 
# below to calculate the logistic growth
# given constant harvesting rate. Use the 
# Forward Euler Method to do this, and make 
# sure that the harvesting stops if the fish 
# go extinct!

import matplotlib.pyplot
import numpy

harvest_rates = [2e4, 5e4, 1e5, 2e5] # tons / year

# This is used to keep track of the data that we want to plot.
data = []

def logistic_growth():
    maximum_growth_rate = 0.5 # 1 / year
    carrying_capacity = 2e6 # tons

    end_time = 10. # years
    h = 0.1 # years
    num_steps = int(end_time / h)
    times = h * numpy.array(range(num_steps + 1))

    fish = numpy.zeros(num_steps + 1) # tons
    fish[0] = 2e5

    for harvest_rate in harvest_rates:
        is_extinct = False

        for step in range(num_steps):
            if is_extinct:
                fish_next_step = 0.
            else:
                fish_next_step = fish[step] + h*(maximum_growth_rate*(1.-(fish[step]/carrying_capacity))*fish[step] - harvest_rate)
                if fish_next_step <= 0.:
                    is_extinct = True
                    fish_next_step = 0.
            fish[step+1] = fish_next_step
            
        data.append(([time for time in times], [f for f in fish], 
            str(harvest_rate)))

    return fish

fish = logistic_growth()


def plot_me():
    fish_plots = []
    for (times, fish, rate_label) in data:
        fish_plots.append(matplotlib.pyplot.plot(times, fish, label=rate_label))    
    matplotlib.pyplot.legend([str(rate) for rate in harvest_rates], loc='upper right')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in years')
    axes.set_ylabel('Amount of fish in tons')
    matplotlib.pyplot.show()

plot_me()
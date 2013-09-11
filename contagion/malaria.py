# PROBLEM 3
# 
# Modify the prevent_malaria function below to 
# implement the Forward Euler Method. 
# 
# At 100 days, mosquito nets are 
# introduced that reduce the probability of
# bites by bite_reduction_by_net.
# 
# Be sure to include this reduction 
# in your model.
#
# Please note that the mosquito population remains 
# constant because its birth rate is equal to
# its mortality rate.

import matplotlib.pyplot

h = 0.1 # days
end_time = 400. # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

total_humans = 1e8
total_mosquitoes = 1e10

def prevent_malaria():
    bites_per_day_and_mosquito = 0.1 # 1 / (day * mosquito)
    transmission_probability_mosquito_to_human = 0.3 # probability
    transmission_probability_human_to_mosquito = 0.5 # probability
    human_recovery_time = 70.0 # days
    mosquito_lifetime = 10.0 # days
    bite_reduction_by_net = 0.9 # probability

    infected_humans = numpy.zeros(num_steps + 1)
    infected_mosquitoes = numpy.zeros(num_steps + 1)

    infected_humans[0] = 0.
    infected_mosquitoes[0] = 1e6

    for step in range(num_steps):
        ###Your code here.
        infected_humans[step + 1] = ###Your code here.
        infected_mosquitoes[step + 1] = ###Your code here.

    return infected_humans, infected_mosquitoes

infected_humans, infected_mosquitoes = prevent_malaria()


def plot_me():
    humans_plot = matplotlib.pyplot.plot(times, infected_humans / total_humans, label='Humans')
    mosquitoes_plot = matplotlib.pyplot.plot(times, infected_mosquitoes / total_mosquitoes, label='Mosquitoes')
    matplotlib.pyplot.legend(('Humans', 'Mosquitoes'), loc='upper right')

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Fraction infected')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    matplotlib.pyplot.show()
plot_me()



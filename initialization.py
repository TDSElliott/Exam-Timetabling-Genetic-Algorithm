"""
Tyler Elliott
2005 3704

Initialize the population with random values
General representation idea of a timetable problem taken from
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.50.5516&rep=rep1&type=pdf
"""

import numpy as np

def create_population(pop_size, num_timeslots, num_exams):
    """Initialize the population

    :param pop_size: how many individuals
    :param num_timeslots: how many timeslots are available
    :param num_exams: how many exams do you have to schedule?
    :return: the population
    """
    # The representation of a chromosome will be a list of length num_exams, where each element will be a number between
    # 0 and num_timeslots - 1. Thus the value x at index i will mean that exam i is scheduled for timeslot x
    population = []
    options = list(range(num_timeslots))

    for _ in range(pop_size):
        # get a random selection of num_exams values that range between 0 and num_timeslots - 1
        population.append(np.random.choice(options, num_exams))

    return population

"""
Tyler Elliott
2005 3704

Select the parents for replacement during evoluton
"""

import random


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """Random uniform selection

    :param current_pop: the original population
    :param current_fitness: the original population fitness
    :param offspring: the children population
    :param offspring_fitness: the children population fitness
    :return: the parents to be replaced during evolution
    """
    population = []
    fitness = []
    combined_pop = current_pop + offspring
    combined_fit = current_fitness + offspring_fitness

    while len(population) < len(current_pop):
        for idx, val in enumerate(combined_pop):
            r = random.choice([0, 1])
            if r == 1:
                population.append(val)
                fitness.append(combined_fit[idx])
                if len(population) == len(current_pop):
                    return population, fitness

    return population, fitness
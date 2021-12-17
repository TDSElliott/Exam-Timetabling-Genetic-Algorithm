"""
Tyler Elliott
2005 3704

Mutate offspring
"""
import random


def mutate(individual, mutation_rate):
    """Iterate through an individual and change bits according to the mutation rate

    :param individual: the individual to mutate
    :param mutation_rate: the rate at which positions should be mutated
    :return:
    """
    for idx, timeslot in enumerate(individual):
        if random.random() < mutation_rate:
            individual[idx] = random.choice(range(21))

    return individual

"""
Tyler Elliott
2005 3704

Find parents to reproduce
"""
import random
from operator import itemgetter


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement

    :param fitness: list of fitness values and individuals
    :param mating_pool_size: how large of a pool to output
    :param tournament_size: how large of a pool to compare from
    :return: parent indices and replacement indices
    """

    selected_to_mate = []
    selected_to_replace = []

    # run 2 tournaments to get the best and worst candidates of each tournament
    while len(selected_to_mate) < mating_pool_size:
        positions = random.sample(range(0, len(fitness)), tournament_size)
        options = [(fitness[position], position) for position in positions]
        i = min(options, key=itemgetter(0))
        idx = i[1]
        selected_to_mate.append(idx)
        j = max(options, key=itemgetter(0))
        idx = j[1]
        selected_to_replace.append(idx)

    return selected_to_mate, selected_to_replace


def relative_to_fitness(population, fitness, mating_pool_size):
    """Select parents relative to their fitness in comparison to the overall population

    :param population: pool of individuals
    :param fitness: fitness for each individual
    :param mating_pool_size: how many we want to select
    :return: indices of parents to mate
    """
    selected_to_mate = random.choices(range(len(population)), weights=fitness, k=mating_pool_size)

    return selected_to_mate


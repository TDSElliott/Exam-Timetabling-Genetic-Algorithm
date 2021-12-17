"""
Tyler Elliott
2005 3704

Recombine parents to produce new offspring
"""
import random


def fixed_point_uniform_crossover(parent1, parent2):
    """Get a random list of positions, if the point is in the list, take from parent 1 for offspring 1

    :param parent1: first parent
    :param parent2: second parent
    :return: two offspring
    """
    chrom_len = len(parent1)
    fpu = chrom_len//2

    offspring1 = []
    offspring2 = []

    positions = random.sample(range(chrom_len), fpu)

    for x in range(len(parent1)):
        if x in positions:
            # Take from parent1 for offpsring1, opposite for offpsring2
            offspring1.append(parent1[x])
            offspring2.append(parent2[x])
        else:
            # it wasn't in the list, take from parent2
            offspring1.append(parent2[x])
            offspring2.append(parent1[x])

    return offspring1, offspring2

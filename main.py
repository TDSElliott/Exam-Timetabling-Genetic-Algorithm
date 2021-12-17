"""
CISC 455 Final Project
Tyler Elliott
2005 3704

A genetic algorithm to solve the time table problem for scheduling exams
"""

import pickle
import time

import numpy as np
import random
import copy


# import your own modules
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection


def main():
    num_timeslots = 21
    num_days = 7  # this is an assumption, i.e., that there are 3 timeslots per day
    num_exams = 180
    num_students = 919

    pop_size = 100
    # mating_pool_size = 2
    mating_pool_size = pop_size//2
    tournament_size = 3
    crossover_rate = 0.9
    mut_rate = 0.05
    max_epochs = 100000

    students = []

    # load student data
    with open("data/yor-f-83-3.stu") as f:
        [students.append(i.strip().split(' ')) for i in f]

    # convert student data to integers
    for idx, x in enumerate(students):
        for y_idx, y in enumerate(x):
            students[idx][y_idx] = int(y)

    # initialize a random population
    # population = initialization.create_population(pop_size, num_timeslots, num_exams)

    # continue from a saved population
    with open('population_20211212-154703.pkl', 'rb') as file:
        population = pickle.load(file)

    for epoch in range(max_epochs):
        fitness_values = evaluation.get_all_fitness(population, students)
        print("generation", epoch, ": best fitness", min(fitness_values), "\taverage fitness", sum(fitness_values) / len(fitness_values))

        combined = list(zip(fitness_values, population))

        # parent selection
        parents_index, replacement_index = parent_selection.tournament(combined, mating_pool_size, tournament_size)
        # parents_index = parent_selection.relative_to_fitness(population, fitness_values, mating_pool_size)

        # uncomment all of the below to try another form of reproduction

        # randomly pair up parents
        # random.shuffle(parents_index)

        # reproduction

        # offspring = []
        # offspring_fitness = []
        i = 0

        # while len(offspring) < mating_pool_size:
        #     # recombination
        #     if random.random() < crossover_rate:
        #         off1, off2 = recombination.fixed_point_uniform_crossover(population[parents_index[i]],
        #                                                                  population[parents_index[i+1]])
        #     else:
        #         off1 = copy.copy(population[parents_index[i]])
        #         off2 = copy.copy(population[parents_index[i+1]])
        #
        #     # mutation
        #     off1 = mutation.mutate(off1, mut_rate)
        #     off2 = mutation.mutate(off2, mut_rate)
        #
        #     # recombination
        #     if random.random() < crossover_rate:
        #         off1, off2 = recombination.fixed_point_uniform_crossover(population[parents_index[0]], population[parents_index[1]])
        #     else:
        #         off1 = copy.copy(population[parents_index[0]])
        #         off2 = copy.copy(population[parents_index[1]])
        #
        #     # mutation
        #     off1 = mutation.mutate(off1, mut_rate)
        #     off2 = mutation.mutate(off2, mut_rate)
        #
        #     offspring.append(off1)
        #     offspring_fitness.append(evaluation.get_fitness(off1, students))
        #     offspring.append(off2)
        #     offspring_fitness.append(evaluation.get_fitness(off2, students))
        #     i += 2
        #
        # population, fitness_values = survivor_selection.random_uniform(population, fitness_values, offspring, offspring_fitness)

        # recombination
        if random.random() < crossover_rate:
            off1, off2 = recombination.fixed_point_uniform_crossover(population[parents_index[i]],
                                                                     population[parents_index[i + 1]])
        else:
            off1 = copy.copy(population[parents_index[i]])
            off2 = copy.copy(population[parents_index[i + 1]])

        # mutation
        off1 = mutation.mutate(off1, mut_rate)
        off2 = mutation.mutate(off2, mut_rate)

        # recombination
        if random.random() < crossover_rate:
            off1, off2 = recombination.fixed_point_uniform_crossover(population[parents_index[0]],
                                                                     population[parents_index[1]])
        else:
            off1 = copy.copy(population[parents_index[0]])
            off2 = copy.copy(population[parents_index[1]])

        # mutation
        off1 = mutation.mutate(off1, mut_rate)
        off2 = mutation.mutate(off2, mut_rate)

        # replace the losers of the tournament with offspring
        population[replacement_index[0]] = copy.copy(off1)
        population[replacement_index[1]] = copy.copy(off2)

        index_min = np.argmin(fitness_values)

        if epoch % 500 == 0:
            # save our population to continue training it
            timestr = time.strftime("%Y%m%d-%H%M%S")
            file_location = 'population_' + timestr + '.pkl'
            with open(file_location, 'wb') as file:
                pickle.dump(population, file)

    # evolution ends
    # save our population to continue training it
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_location = 'population_' + timestr + '.pkl'
    with open(file_location, 'wb') as file:
        pickle.dump(population, file)

    print("The best exam timetable is", population[index_min], "with fitness", fitness_values[index_min])

if __name__ == "__main__":
    main()
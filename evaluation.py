"""
Tyler Elliott
2005 3704

Calculate fitness of a potential solution. Fitness will be a punishment value (i.e., error) to be minimized.
"""
import numpy as np


def get_all_fitness(population, students):
    """Return the fitness for each individual in the population

    :param population: all individuals
    :param students: a list of students and their exams
    :return: list of fitnesses
    """
    all_fitness = []
    for individual in population:
        all_fitness.append(get_fitness(individual, students))
    return all_fitness


def get_fitness(individual, students):
    """The fitness value of an individual

    :param individual: One chromosome
    :param students: a list of students and their exams
    :return: individual fitness
    """
    # penalties
    two_exams_at_once = 30
    more_than_two_a_day = 10
    two_consecutive_same_day = 3

    fitness = 0

    for student in students:
        # for each student we need to evaluate number of conflicts
        # two at same time
        seen = []
        for exam in student:
            if individual[exam-1] in seen:
                fitness += two_exams_at_once
            else:
                seen.append(exam-1)
        # more than two a day
        days = np.zeros(7)
        for exam in student:
            timeslot = individual[exam-1]
            day = timeslot // 3
            days[day] += 1
        # go through each day
        for day in days:
            # if there are more than 2 exams that day
            if day > 2:
                # add the penalty proportional to the number of exams > 2
                fitness += more_than_two_a_day * (day-2)

        # two consecutive in 1 day
        exam_times = []
        for exam in student:
            exam_times.append(individual[exam-1])
        for exam in student:
            exam_times.remove(individual[exam-1])
            for time_slot in exam_times:
                if individual[exam-1]//3 == time_slot//3 and (individual[exam-1] == time_slot-1 or individual[exam-1] == time_slot + 1):
                    fitness += two_consecutive_same_day

    return fitness
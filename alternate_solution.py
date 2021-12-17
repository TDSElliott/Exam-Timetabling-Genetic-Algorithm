import numpy as np

import evaluation

def conflict(individual, students):
    # penalties
    two_exams_at_once = 30
    more_than_two_a_day = 10
    two_consecutive_same_day = 3
    num_timeslots = 21

    fitness = 0
    epochs = 0

    print("Starting fitness", evaluation.get_fitness(individual, students))

    zero_conflicts = False
    while not zero_conflicts:
        epochs += 1
        conflicts = False
        for student in students:
            # for each student we need to evaluate number of conflicts
            # two at same time
            seen = []
            for exam in student:
                if individual[exam - 1] in seen:
                    conflicts = True
                    individual[exam-1] = np.random.randint(0, num_timeslots)
                else:
                    seen.append(exam - 1)
            # more than two a day
            days = np.zeros(7)
            for exam in student:
                timeslot = individual[exam - 1]
                day = timeslot // 3
                days[day] += 1
            # go through each day
            for day in days:
                # if there are more than 2 exams that day
                if day > 2:
                    # add the penalty proportional to the number of exams > 2
                    conflicts = True
                    individual[exam-1] = np.random.randint(0, num_timeslots)

            # two consecutive in 1 day
            exam_times = []
            for exam in student:
                exam_times.append(individual[exam - 1])
            for exam in student:
                exam_times.remove(individual[exam - 1])
                for time_slot in exam_times:
                    if individual[exam - 1] // 3 == time_slot // 3 and (
                            individual[exam - 1] == time_slot - 1 or individual[exam - 1] == time_slot + 1):
                        conflicts = True
                        individual[exam - 1] = np.random.randint(0, num_timeslots)
        if not conflicts:
            zero_conflicts = True
        print("Fitness after epoch", epochs, ":", evaluation.get_fitness(individual, students))


def test_conflict():
    students = []

    with open("data/yor-f-83-3.stu") as f:
        [students.append(i.strip().split(' ')) for i in f]

    for idx, x in enumerate(students):
        for y_idx, y in enumerate(x):
            students[idx][y_idx] = int(y)

    num_timeslots = 21
    num_exams = 180
    options = list(range(num_timeslots))

    # get a random selection of num_exams values that range between 0 and num_timeslots - 1
    solution = np.random.choice(options, num_exams)

    conflict(solution, students)

test_conflict()
example_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
example_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
example_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]


def school_grades(results):
    new_grades = []
    for i in results:
        if i == 3:
            new_grades.append(4)
            continue
        if i == 2: continue
        new_grades.append(i)
    return new_grades


print('example_1 =', school_grades(example_1))
print('example_2 =', school_grades(example_2))
print('example_3 =', school_grades(example_3))

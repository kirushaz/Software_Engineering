x1 = ((1, 2, 3), 1)
x2 = ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
x3 = ((2, 4, 6, 6, 4, 2), 9)


def nikolai(value):
    source_tuple, element = value

    new = []
    was_removed = False
    for x in list(source_tuple):
        if x == element and was_removed == False:
            was_removed = True
            continue
        new.append(x)

    return tuple(new)


print('Вариант 1 =', nikolai((x1)))
print('Вариант 2 =', nikolai((x2)))
print('Вариант 3 =', nikolai((x3)))

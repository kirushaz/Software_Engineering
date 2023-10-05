x1 = ((1, 2, 3), 8)
x2 = ((1, 8, 3, 4, 8, 8, 9, 2), 8)
x3 = ((1, 2, 8, 5, 1, 2, 9), 8)


def office (value):
    source_order, id = value
    was_first_check = False

    new = []
    for x in list(source_order):
        if x == id and was_first_check:
            new.append(x)
            break

        if x == id: was_first_check = True

        if was_first_check:
            new.append(x)

    return tuple(new)


print('X 1=', office(x1))
print('X 2=', office(x2))
print('X 3=', office(x3))

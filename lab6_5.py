x = (5, 34, 51, 23, 11, 10)


def get_even_numbers(values):
    new = []

    for x in list(values):
        if x > 10: new.append(x)

    return tuple(new)

print('Числа больше 10', get_even_numbers(x))


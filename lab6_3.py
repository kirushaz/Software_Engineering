import collections

def number(value):
    new = {}
    for x in value:
        number = int(x)
        if number in new: new[number] = new[number] + 1
        else: new[number] = 1
    new_to_list = list(new.items())
    new_to_list.sort(reverse=True, key=lambda x: x[1])

    values = new_to_list[0:3]
    values.sort(key=lambda x: x[0])

    return collections.OrderedDict(values)

result = number(input('Введите последовательность чисел: '))

for x in result.items():
    print(f'Число {x[0]} встретилось {x[1]} раз(а)')

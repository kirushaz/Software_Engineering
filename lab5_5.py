list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def set1(value):
    result = set()

    while len(value) > 1:
        element = value.pop(0)
        element_count = value.count(element)
        result.add(element)
        for i in range(element_count):
            result.add(str(element) * (i + 2))

    return result

print('Список 1:', set1(list_1))
print('Список 2:', set1(list_2))
print('Список 3:', set1(list_3))

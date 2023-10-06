def calcul(x):
    try:
        converted_value = int(x)

        return 2 + converted_value;
    except ValueError as error:
        print('Не верный тип данных. Нужно число.')

print(calcul(2))
print(calcul('5345'))
print(calcul('число'))

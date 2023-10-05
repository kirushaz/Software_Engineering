with open('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic7/1.txt', 'a') as f:
    cat = input('Категория ')
    date = input('Дата ')
    summa = int(input('Сумма '))

    f.write(f'{date}\t{cat}\t{summa}\n')

with open('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic7/1.txt', 'r') as f:
    print('Записано:\n', f.read())

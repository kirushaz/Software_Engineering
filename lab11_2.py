def fib(n):
    x = 1
    y = 1
    for z in range(n):
        total = x
        x, y = y, x + y
        yield total

print('Готово')
with open('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic11/1.txt', 'a') as f:
    for give in fib(653):
        f.write(f'{give}\n')
    print('Записано в файл', give)




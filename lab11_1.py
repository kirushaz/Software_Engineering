def fib(n):
    x = 1
    y = 1
    for z in range(n):
        total = x
        x, y = y, x + y
        yield total

print('Готово')
for give in fib(653):
    print(give)

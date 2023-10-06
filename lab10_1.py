import time
def mesuare(q):
    def vova(*args, **kwargs):
        start = time.time()
        y = q(*args, **kwargs)
        end = time.time()
        x = end - start
        print(f'\nВремя выполнения {x} ')
        return y
    return vova
@mesuare
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

if __name__ == '__main__':
    fibonacci()

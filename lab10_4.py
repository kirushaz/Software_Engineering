def tupe(fun):
    def x(*args, **kwargs):
        y = fun(*args, **kwargs)
        print('Тип ', type(y))
        return y
    return x
@tupe
def numbers(a, b):
    return a + b
@tupe
def strings(a, b):
    return a + b
strings('world', 'hello')
numbers(67, 56)

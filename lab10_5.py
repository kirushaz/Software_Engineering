class soob(Exception):
    def __init__(self, message):
        self.message = message

def user(value):
    if len(value) < 11:
        raise soob('Длина сообщения больше 10-ух символов')

class mess:
    def __init__(self, mes):
        self.name = user(mes)

try:
    user('hello')
except soob as error:
    print('Ошибка:', error)

try:
    mess('helloworld..')
except soob as error:
    print('Ошибка:', error)

finally:
    print('Предложение введенно верно')

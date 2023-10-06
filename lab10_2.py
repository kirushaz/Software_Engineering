class Error(Exception):
    def __init__(self, text):
        self.message = text

def file(path, mode):
    try:
        with open(path, mode) as f:
            x = f.read()
            if x == '':
                raise Error('Файл пуст')
            else:
                print('В файле содержится текст=', x)
    except Error as error:
        print('Ошибочка:', error)

file('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic10/1.txt', 'r')
file('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic10/2.txt', 'r')

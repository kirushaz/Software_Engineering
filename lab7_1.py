import re
def word(txt):
    text = {}
    for i in txt:
        if i in text: text[i] = text[i] + 1
        else: text[i] = 1
    dictionary_to_list = list(text.items())
    dictionary_to_list.sort(reverse=True, key=lambda x: x[1])

    return dictionary_to_list[0:1][0]

with open ('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic7/n.txt', 'r') as file:
    new = file.read()
    content_without_spectial_chars = re.sub(r'[^a-zA-Zа-яА-я0-9]', '  ', new)
    spaces = re.sub(r' {2,}', ' ', content_without_spectial_chars)
    m = spaces.split(' ')
    often_word = word(m)
    print(f'Чаще всего встречается  "{often_word[0]}". Оно встречается {often_word[1]} раз '  ', всего слов = ', len(m))

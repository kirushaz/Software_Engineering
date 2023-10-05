x= 'Hello, world! Python IS the programming language of thE future. My\nEMAIL is....\nPYTHON is awesome!!!!'

with open('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic7/text.txt', 'r') as f:
    word = f.read().split(' ')
    text = x.lower()
    for word in word:
        text = text.replace(word, '*' * len(word))
    y = ''
    for i, word in enumerate(text):
        if x[i].lower() == word:
            y += x[i]
        else:
            y += word

    print(y)

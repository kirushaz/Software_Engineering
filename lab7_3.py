abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

with open('/Users/kirillzuev/Desktop/синх/7 семестр/Программная инженерия/pic7/6.txt', 'r') as f:
    lines = f.readlines()
    letters = 0
    words = 0

    for line in lines:
        for word in line.strip():
            if word.lower() in abc:
                letters += 1
        words += len(line.split(' '))

    print('Input file contains:')
    print(f'{letters} letters')
    print(f'{words} letters')
    print(f'{len(lines)} lines')

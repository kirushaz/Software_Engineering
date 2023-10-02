a=str (input('Введите предложение на английском '))
print(len(a))
print(a.casefold())
count = 0
vowels = set("aeiouAEIOA")
for letter in a:
    if letter in vowels:
        count += 1
print("Количество гласных равно:")
print(count)
b=a.replace ('ugly', 'beauty')
print(b)
prefixes = ('the')
print(b.startswith(prefixes))
result = b.endswith('end')
print(result)

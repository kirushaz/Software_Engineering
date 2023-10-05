from math import sqrt


def calc(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print(
    'S_MAX=',
    calc(max(one), max(two), max(three))
)
print(
    'S_MIN=',
    calc(min(one), min(two), min(three))
)

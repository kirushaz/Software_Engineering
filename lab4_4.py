def average(*num):
    total = 0
    for q in num:
        total += q
    return total / len(num)

if __name__ == '__main__':
    res = average (4,6)
    print("Среднее значение")
    print(res)

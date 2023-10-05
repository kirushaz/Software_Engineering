results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
best = []
for i in range(3):
    best_result = min(results)
    best.append(best_result)
    results.remove(best_result)
print('Три лучших ', best)
worst = []
for i in range(3):
    worst_result = max(results)
    worst.append(worst_result)
    results.remove(worst_result)
print('Три худших ', worst)
more10 = []
for i in results:
    if i >= 10.01: more10.append(i)
print('Все результаты начиная с 10 секунд', more10)

import random
def kubik():
    throw = random.randint(1, 6)
    print(f"Выпало {throw}")
    if throw == 1 or throw == 2:
        print("Проигрыш")
    elif throw == 5 or throw == 6:
        print("Выигрыш")
    else:
        print("Еще раз")
        kubik()
if __name__ == '__main__':
    kubik()

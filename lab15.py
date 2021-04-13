import random

COUNT = 5
n = random.randint(0, 100)
try_n = -1
while(COUNT>0 and try_n!=n):
    try_n=int(input("Введите число "))
    if(try_n<n):
        print("Загаданное число больше")
        COUNT=COUNT-1
    if(try_n>n):
        print("Загаданное число меньше")
        COUNT = COUNT - 1
    if(try_n==n):
        print("Поздравляю! Вы угадали")
        x = input("Хотите начать сначала? (1 - ДА, 2 - НЕТ )")
        x = int(x)

        if x == 2:
            print("Спасибо за игру")
        if x == 1:
            COUNT=5
            try_n=-1
            continue
    if(COUNT==0):
        print("Вы проиграли. Было загадано: ",n)
        x = input("Хотите начать сначала? (1 - ДА, 2 - НЕТ )")
        x = int(x)

        if x == 2:
            print("Спасибо за игру")
        if x == 1:
            COUNT = 5
            try_n = -1
            continue



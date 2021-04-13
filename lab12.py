n = int(input("Введите целое положительное число "))
if (n>0 and n%1==0):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print("Факториал числа =", factorial)
else:
    print("Введены некорректные данные!")
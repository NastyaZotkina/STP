import math

stroka=input().split()
a=float(stroka[0])
b=float(stroka[2])
znak=stroka[1]
if znak == '+':
    if (math.fmod(a+b, a+b) == 0):
        print(math.floor(a+b))
    else:
        print(a + b)
elif znak == '-':
    if (math.fmod(a-b, a-b) == 0):
        print(math.floor(a-b))
    else:
        print(a-b)
elif znak == '*':
    if (math.fmod(a*b, a*b) == 0):
        print(math.floor(a*b))
    else:
        print(a*b)
elif znak == '/':
    if (b==0):
        print("Деление на ноль!")
    elif(math.fmod(a/b, a/b) == 0):
        print(math.floor(a/b))
    else:
        print(a/b)
else:
    print("Некорректный ввод")

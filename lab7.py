import math
print("Нажмите 1 для нахождения площади треугольника через его стороны или нажмите 2 для нахождения площади через вершины:")
x=input("Сделайте Ваш выбор ")
x=int(x)

if x==1:
    a=float(input("Введите сторону a "))
    b = float(input("Введите сторону b "))
    c = float(input("Введите сторону c "))
    if(a>0 and b>0 and c>0):
        p=(a+b+c)/2
        if(a+b>c and a+c>b and b+c>a):
            S=math.sqrt(p*(p-a)*(p-b)*(p-c))
            if (math.fmod(S, S) == 0):
                S = math.floor(S)
            print("S =", S)
        else:
            print("Треугольник не существует")
    else:
        print("Были введены некорректные данные!")
elif x==2:
    print("Введите координаты вершин треугольника:\n")
    k1 = input("Координаты первой вершины ").split()
    x1=float(k1[0])
    y1=float(k1[1])
    k2 = input("Координаты второй вершины ").split()
    x2=float(k2[0])
    y2=float(k2[1])
    k3 = input("Координаты третьей вершины ").split()
    x3=float(k3[0])
    y3=float(k3[1])
    S=math.fabs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
    if((x1==x2 and y1==y2)or(x2==x3 and y2==y3)or(x1==x3 and y1==y3)):
        print("Треугольник не существует")
    else:
        if (math.fmod(S, S) == 0):
            S = math.floor(S)
        print("S =", S)
else:
    print("Введены некорректные данные. Ошибка!")



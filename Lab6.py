import math

a=float(input("Введите а:"))
b=float(input("Введите b:"))
c=float(input("Введите c:"))
if (a!=0 and b!=0 and c!=0):
    D=b*b-4*a*c
    if(D>0):
        x1 = (-b + math.sqrt(D)) / (2 * a)
        if(math.fmod(x1,x1)==0):
            x1=math.floor(x1)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        if (math.fmod(x2, x2) == 0):
            x2 = math.floor(x2)
        print("x1=", x1, "\n", "x2=", x2)
    elif(D==0):
        x1 = (-b)/(2*a)
        print("x=", x1)
    elif(D<0):
        print("Нет действительных корней")
elif (a == 0 and b!=0 and c!=0):
        print(-c / b)
elif(a !=0 and b == 0 and c != 0):
        print(math.sqrt(-c/b))
elif(a==0 and b==0 and c==0):
    print("Все числа = 0")



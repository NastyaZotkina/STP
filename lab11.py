print("Нажмите 1, если возводимое в степень число целое или нажмите 2, если оно дробное:")
x=input("Сделайте Ваш выбор ")
x=int(x)

if x==1:
    a=int(input("Введите число, возводимое в степень "))
    b=int(input("Введите степень "))
    print("a^b=",a**b)
elif x==2:
    a=float(input("Введите число, возводимое в степень "))
    b=int(input("Введите степень "))
    print("a^b=",a**b)
else:
    print("введены некорректные данные!")
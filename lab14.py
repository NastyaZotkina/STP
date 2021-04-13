import math
X=1
I=0
n=int(input("введите n: "))
if(n>=0 and n<=math.pow(10,15)):
    while X<=n:
        X=X*2
        I=I+1
    print(I)
else:
    print("введены некорректные данные")
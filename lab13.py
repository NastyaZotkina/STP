n = int ( input ("Введите число n: "))

for i in range (2, n):

    if (n % i) == 0:

        print ("Число ", n, "не простое")

        break

    elif (n // i) == 1:

        print ("Число ", n, " простое!")

        break 
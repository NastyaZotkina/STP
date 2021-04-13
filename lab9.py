h1 = list(map(int, input().split(':')))
h2 = list(map(int, input().split(':')))

m1 = h1[0]*3600+h1[1]*60
m2 = h2[0]*3600+h2[1]*60

interval = m2-m1
minute = interval // 60
if minute <= 10:
    print("Встреча состоится")
else:
    print("Встреча не состоится")
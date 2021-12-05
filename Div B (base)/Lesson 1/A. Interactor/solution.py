r = int(input())
i = int(input())
c = int(input())

if (i == 0 and r == 0) or i == 1:
    print(c)
elif (i == 0 or i == 4) and r != 0:
    print(3)
elif i == 6 or i == 7:
    print(i % 2)
else:
    print(i)
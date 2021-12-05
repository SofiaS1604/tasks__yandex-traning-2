d = int(input())
a, b = map(int, input().split())

if 0 <= a <= d and 0 <= b <= -a + d:
    print(0)
else:
    mod = (a ** 2 + b ** 2) ** 0.5
    ax = ((a - d) ** 2 + b ** 2) ** 0.5
    bx = (a ** 2 + (b - d) ** 2) ** 0.5
    if min(mod, ax, bx) == mod:
        print(1)
    elif min(mod, ax, bx) == ax:
        print(2)
    elif min(mod, ax, bx) == bx:
        print(3)

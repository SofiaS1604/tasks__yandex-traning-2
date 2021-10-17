num = int(input())
pupils = list(map(int, input().split()))

if num % 2 != 0:
    med = int(num // 2)
else:
    med = int(num / 2)

print(pupils[med])
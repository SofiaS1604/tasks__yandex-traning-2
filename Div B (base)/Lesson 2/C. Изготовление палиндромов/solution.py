string = list(input())
price = 0

if len(string) > 0:
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            price += 1
print(price)
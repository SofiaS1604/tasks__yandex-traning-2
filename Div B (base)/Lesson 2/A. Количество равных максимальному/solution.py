max_number = 0
count_max_number = 1
n = 1

while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
        count_max_number = 1
    elif max_number == n:
        count_max_number += 1
print(count_max_number)
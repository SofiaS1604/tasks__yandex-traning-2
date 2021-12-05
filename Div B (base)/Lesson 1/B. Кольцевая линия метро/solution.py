N, i, j = map(int, input().split())

max_num = max(i, j)
min_num = min(i, j)

k = min(abs(i - j) - 1, (N - max_num + min_num) - 1)
print(k)
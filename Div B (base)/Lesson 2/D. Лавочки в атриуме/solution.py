l, k = map(int, input().split())
a = list(map(int, input().split()))
left_center = l // 2 + l % 2 - 1
right_center = l - l // 2 - l % 2
left_leg = -1
right_leg = -1
legs = []

for i in range(k):
    if a[i] <= left_center:
        left_leg = a[i]
    if (a[i] >= right_center) and (right_leg == -1):
        right_leg = a[i]

if left_leg != -1:
    legs.append(left_leg)
if (right_leg != -1) and (right_leg != left_leg):
    legs.append(right_leg)

print(' '.join(str(leg) for leg in legs))
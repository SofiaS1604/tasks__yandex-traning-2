nums = list(map(int, input().split()))
nums_distance = [0] * len(nums)
left_shop = -100
right_shop = 100

for i in range(0, len(nums) - 1):
    if nums[i] == 2:
        left_shop = i
    elif nums[i] == 1:
        nums_distance[i] = i - left_shop

for i in range(len(nums) - 1, -1, -1):
    if nums[i] == 2:
        right_shop = i
    elif nums[i] == 1:
        nums_distance[i] = min(nums_distance[i], right_shop - i)

print(max(nums_distance))
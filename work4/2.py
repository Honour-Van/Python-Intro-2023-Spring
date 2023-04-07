n = int(input())

nums = []
line = input().split()
for num in line:
    nums.append(int(num))

max_num = 0
min_num = 1001
for num in nums:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(max_num - min_num)
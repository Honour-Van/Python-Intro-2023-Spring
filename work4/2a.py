n = int(input())

nums = []
line = input().split()
for num in line:
    nums.append(int(num))

max_num = max(nums)
min_num = min(nums)

print(max_num - min_num)
n = int(input())
stat = {}
for i in range(1, n+1):
    nums = list(map(int, input().split(',')))
    for num in nums:
        stat[num] = stat.get(num, []) + [i]
result = sorted(list(stat.items()))[-1]
print(result[0])
print(','.join(str(i) for i in sorted(list(set(result[1])))))
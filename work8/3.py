day1 = input()
num = len(day1)
day2 = ''
i = 0
while i < num:
    if day1[i] == '*':
        if i > 0 and day2[i-1] != '*':
            day2 = day2[:-1] + '*'
        day2 += '*'  # 本质上只需要对位更新。旁边两个分支都是在考虑扩散的情况
        if i < num-1 and day1[i+1] != '*':
            day2 += '*'
            i += 1
    else:
        day2 += '#'
    i += 1
print(day2.count('#'))


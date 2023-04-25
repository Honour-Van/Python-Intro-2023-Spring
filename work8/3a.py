day1 = input()
num = len(day1)
day2 = ''
i = 0
for i in range(num):
    cur = '#'
    if day1[i] == '*':
        cur = '*'
    elif i > 0 and day1[i-1] == '*':
        cur = '*'
    elif i < num-1 and day1[i+1] == '*':
        cur = '*'
    day2 += cur
print(day2.count('#'))


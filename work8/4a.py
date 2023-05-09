# 使用函数封装以及defaultdict
from collections import defaultdict

# 输入
n, m = map(int, input().split())
code = [int(i) for i in input().split()]

# 输出
light_first = code[0]
light_last = 0

# 数据结构初始化
lamp0 = defaultdict(int)
lamp0[code[0]] = 1

s = 1


def check(i):
    if i == 1 and (lamp0[n] == 1 or lamp0[2] == 1):
        return True
    elif i == n and (lamp0[n-1] == 1 or lamp0[1] == 1):
        return True
    elif lamp0[i-1] == 1 or lamp0[i+1] == 1:
        return True
    return False


def work(i):
    global s
    lamp0[i] = 1
    s += 1


for i in code[1:]:
    if lamp0[i] == 1:  # 要判断是不是已经亮了，不然会重复计数
        continue

    # 有较多的重复代码，可以考虑用函数封装
    # 这里只是为了演示使用函数的思想，做题的时候不一定要这么写
    if check(i):
        work(i)

    if s == n:
        light_last = i
        break

if s >= n:
    print(light_first, light_last)  # sep 默认是空格
else:
    print("No")

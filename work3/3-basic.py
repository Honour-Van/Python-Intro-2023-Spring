# @file: 3-basic.py
# @author: fhn
# 一个简单的模拟类问题

n = int(input())
for i in range(n): # 类似第一题 也可以使用while循环
    s = int(input())
    timebike = 27 + 23 + s/3
    timewalk = s/1.2
    # 展示完整的三种分支控制
    if timebike < timewalk:
        result = "Bike"
    elif timebike > timewalk:
        result = "Walk"
    else:
        result = "All"
    print(result)
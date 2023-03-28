# @file: 5.py
# @credit: 2000015176
# 本题的退出条件就是不确定的，适合使用while循环，同样是一道模拟类问题

n = int(input())
while n != 1:
    if n % 2 == 0:
        print(str(n) + "/2=" + str(n // 2))
        n = n // 2
    else:
        print(str(n) + "*3+1=" + str(n * 3 + 1))
        n = n * 3 + 1
print("End")

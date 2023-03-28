# @file: 1-while.py while 循环版本
# @author: fhn

n = int(input())
i = 0
ans = 0
while i < n:
    i += 1  # 本质和for循环是一样的，不过手动维护i每次加1的操作
    ans += int(input())
print(ans)

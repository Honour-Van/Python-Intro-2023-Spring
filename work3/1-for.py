# @file: 1-for.py 循环版本
# @author: fhn

n = int(input())   # 输入数目
ans = 0            # 保存答案
for i in range(n): # range(n) 默认是0到n，保证n次即可，不用(1,n+1)
    ans = ans + int(input()) # 直接写，也可以先输入为一个中间变量
print(ans)
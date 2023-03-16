# 一个传统的做法
# n = int(input())
# print(n // 100)
# print(n % 100 // 10)
# print(n % 10)

# 理解input输入的是字符串，所以可以直接输出
n = input()
for i in n:
    print(i)
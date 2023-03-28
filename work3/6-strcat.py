# @file: 6-strcat.py 使用字符串拼接实现
# @credit: 2200017492

n = int(input())
for i in range(1, n+1):
    print("." * (n-i) + "#" * n + "."*(i-1))
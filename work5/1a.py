# 暂时通不过OJ的进阶版
price = [28.9, 32.7, 45.6, 78, 35, 86.2, 27.8, 43, 56, 65]
print(f'{sum([price[i] * int(x) for i, x in enumerate(input().split())]):.1f}')

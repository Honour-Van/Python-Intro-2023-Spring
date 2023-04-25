price = [28.9, 32.7, 45.6, 78, 35, 86.2, 27.8, 43, 56, 65]
res = 0
book_num = [int(x) for x in input().split()]
for i in range(10):
    res += price[i] * book_num[i]
# print('{:.1f}'.format(res))
print(f'{res:.1f}')
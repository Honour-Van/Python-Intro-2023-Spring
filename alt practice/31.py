# @file: 31.py 奇数求和

m = int(input())
n = int(input())
ans = 0
if m < n:
    for s in range(m, n+1):
        if s % 2 == 1:
            ans += s
else:
    for s in range(n, m+1):
        if s % 2 == 1:
            ans += s
print(ans)

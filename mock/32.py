n, a = input().split()
n, a = int(n), int(a)
ans = 0
for i in range(1, n+1):
    ans += int(str(a)*i)
print(ans)
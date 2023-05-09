n = int(input())
a = int(input())
ans = 0
curm = a
cura = a
for i in range(1, n+1):
    ans += curm
    cura += 1
    curm *= cura
print(ans)
# 用01数组来模拟道路上的树，0 无树，1 有树，然后遍历区间，将区间内的树去掉，最后统计剩下的树的数量即可
lenth, regionnum = input().split()
lenth, regionnum = int(lenth), int(regionnum)
s = []

for i in range(0,lenth+1):
    s.append(1)
for y in range(0,regionnum):
    m,n = input().split()
    m,n = int(m),int(n)
    o = n-m+1
    l = []
    for i in range(0,o):
        l.append(0)
    s[m:n+1] = l
s = [x for x in s if x==1]
print(len(s))
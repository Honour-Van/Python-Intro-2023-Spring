# 合并区间
L, M = map(int, input().split())
shu = L + 1
lst = []
for i in range(M):
    lst1 = input().split()
    lst1 = [int(j) for j in lst1]
    cha = lst1[1] - lst1[0]
    lst.append(lst1)
lst2 = sorted(lst, key=lambda x: (x[0]))

i = 1
while i < len(lst2):
    if lst2[i][0] <= lst2[i-1][1]:
        lst2[i-1][1] = max(lst2[i][1], lst2[i-1][1])
        lst2.pop(i)
    else:
        i += 1

b = 0
de = 0
a = len(lst2)
while b < a:
    de = de + lst2[b][1] - lst2[b][0] + 1
    b += 1
sheng = shu - de
print(sheng)

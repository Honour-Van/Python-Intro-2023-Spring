# 斐波那契 递推版
n = int(input())
ans = 0

young = 1
mature = 0

last_young = young
last_mature = 0

for i in range(n):
    ans = young + mature
    mature += last_young  # 年轻兔子成熟了
    young = last_mature  # 成熟兔子会继续生育
    last_mature = mature
    last_young = young
print(ans)

m = int(input())
n = int(input())

# 辗转相除法，如果n小于m会把n和m的值交换
while (m != 0):
    r = n % m
    n = m
    m = r
print(n)
def gcd(n, m):
    while (m != 0):
        # 计算
        r = n % m
        print(f"{n}/{m}={n // m}...{r}")
        # 更新
        n = m
        m = r
    return n


n, m = input().split()
n, m = int(n), int(m)
print(gcd(n, m))

def gcd(n, m):
    if m == 0:
        return n
    else:
        print(f"{n}/{m}={n // m}...{n % m}")
        return gcd(m, n % m)
n, m = input().split()
n, m = int(n), int(m)
print(gcd(n, m))

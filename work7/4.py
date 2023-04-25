def isPrime(n):
    if str(n) != str(n)[::-1]:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
ans = 0
for i in range(11, n+1):
    if isPrime(i):
        ans += 1
print(ans)
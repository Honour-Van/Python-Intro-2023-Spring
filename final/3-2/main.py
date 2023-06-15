cur = 0
ans = 0
symbol = 1
    
n = int(input())
for i in range(1, n+1):
    cur += i
    ans += symbol * 1 / cur
    symbol *= -1
print(f'{ans:.10f}')
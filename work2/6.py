bar = [0, 100000, 200000, 400000, 600000, 1000000, 100000000000]
profit = [0, 0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

n = int(input())
ans = 0

for i in range(7):
    if n < bar[i]:
        ans += profit[i] * (n - bar[i-1])
        break
    else:
        ans += profit[i] * (bar[i] - bar[i-1])

print(f"{ans:.2f}") 
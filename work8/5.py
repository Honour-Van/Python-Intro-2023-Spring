def solve(cur, day):
    if day == 1:
        return cur
    return solve((cur + 1) * 2, day - 1)
t = int(input())
for i in range(t):
    n = int(input())
    print(solve(1, n))
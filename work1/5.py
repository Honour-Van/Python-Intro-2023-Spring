import math

n, x, y = input().split()
n = int(n)
x = int(x)
y = int(y)
# an advanced impl.
# n, x, y = [int(i) for i in input().split()]

eaten = math.ceil(y / x)
print(n - eaten)

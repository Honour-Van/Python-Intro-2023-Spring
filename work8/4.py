n, m = map(int, input().split())
num = n
lights = [0] * (n + 1)

s, e = 0, 0
def check(k):
    if lights[k] == 1:
        return False
    left = k-1
    right = k+1
    if left < 1:
        left = n
    if right > n:
        right = 1
    if lights[left] == 1 or lights[right] == 1:
        return True
    return False

for i in map(int, input().split()):
    if num == n:
        lights[i] = 1
        num -= 1
        s = i
    elif check(i):
        lights[i] = 1
        num -= 1
    if num == 0:
        e = i
        break
if s == 0 or e == 0:
    print("No")
else:
    print(s, e)
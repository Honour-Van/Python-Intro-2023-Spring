# @credit 2000014186
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a, b, i = 1, 2, 2
    while i < n:
        a, b = b, a + b
        i += 1
    print(b)
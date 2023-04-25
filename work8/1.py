def check(n):
    s =  0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
def solve(n):
    flag = False
    for i in range(1, n):
        if check(i):
            flag = True
            print(i)
    if not flag:
        print('No')

solve(int(input()))


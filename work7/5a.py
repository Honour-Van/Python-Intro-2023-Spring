# @credit: 赵君
def count_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stairs(n-1) + count_stairs(n-2)

n = int(input())
print(count_stairs(n))
# 使用组合数求解

from math import comb

def climb_stairs_comb(n: int) -> int:
    max_twos = n // 2
    total_ways = 0
    for twos in range(max_twos + 1):
        ones = n - 2 * twos
        total_ways += comb(ones + twos, twos)
    return total_ways

n = int(input())
print(climb_stairs_comb(n))

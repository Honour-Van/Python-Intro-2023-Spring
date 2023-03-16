import math

Pi = 3.14159
h, r = [int(i) for i in input().split()]
print(math.ceil(20 * 1000 / (Pi * r * r * h)))
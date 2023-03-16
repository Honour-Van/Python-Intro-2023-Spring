n = int(input())
paper = 0.0003
folded = paper * (2 ** n)

print(f"{folded:.2f}") # 问题就在这个精度控制
print(folded - 8848.86 > 1e-5)
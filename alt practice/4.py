n = int(input())
paper = 0.0003
folded = paper * (2 ** n)

print(folded) # 这个题目比第3题简单，不需要精度控制
print(folded - 8848.86 > 1e-5)
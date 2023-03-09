n = int(input())
paper = 0.0003
folded = paper * (2 ** n)

print("%.2f" % folded)
print(folded - 8848.86 > 1e-5)
# 使用列表完成
# @credit: 2200013918

n = int(input())
data = []
names = []
for i in range(n):
    name, score = input().split()
    name = name.capitalize()
    if name in names:
        continue
    names.append(name)
    data.append((name, int(score)))
data.sort(key=lambda x: (-x[1], x[0][0].lower(), len(x[0])))
print("Name\tScore")
for d in data:
    print("{}\t{}".format(d[0].capitalize(), d[1]))
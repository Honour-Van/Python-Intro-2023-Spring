string = input()
cut = input()
D = {}

for i in string:  # 字符串可以遍历的哦
    D[i] = D.get(i, 0) + 1  # 使用get设置默认值的方式简化统计

for c in cut:  
    if c in D.keys():
        D.pop(c)  # 更常用的是使用pop函数

sorted_D = sorted(D.items(), key=lambda x: x[1], reverse=True)
for items in sorted_D:
    print(items[0] + ' ', items[1])  # 逗号默认是一个空格
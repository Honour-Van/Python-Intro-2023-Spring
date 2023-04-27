n = int(input())
name_dict = {}
for i in range(n):
    name, score = input().split()
    name = name.capitalize() # 首字母大写，其余小写
    if name in name_dict: # 剔除重名
        continue
    name_dict[name] = score
scores = sorted(name_dict.items(), key=lambda x: (-int(x[1]), x[0][0], len(x[0])))
# 排序规则：成绩由高到低，姓名首字母从小到大，姓名长度从短到长
print("Name\tScore")
for name, score in scores:
    print("{}\t{}".format(name, score))

# 使用collections.defaultdict() #39581366
# @credit: 2100017723 陈徐磊
from collections import defaultdict

# 使用collections.defaultdict()方法生成字典，避免数据覆盖
score_dict = defaultdict(list)

# 获取输入，将输入存储在字典中
amount = int(input())
for i in range(amount):
    name, score = input().split()
    score_dict[str(name).capitalize()].append(int(score))

# 从字典中取出特定的数据（成绩的第一个输入）并排序，存储在列表中
score_list = sorted([(j[0], j[1][0]) for j in score_dict.items()], key=lambda x: (-x[1], x[0][0], len(x[0])))

# 输出，使用f-string格式化
print("Name\tScore")
for k in score_list:
    print(f"{k[0]}\t{k[1]}")
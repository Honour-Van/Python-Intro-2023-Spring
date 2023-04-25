'''
英语课的期末考试结束后，你帮老师录入学生成绩信息。手写的英文名被AI识别后得到一些原始数据，包括学生的姓名和成绩。AI程序在识别过程中受到了一些未知因素干扰，导致大小写导出时出现了未知问题，你需要编写这个AI流水线的下一级，把原始数据整理成美观的表格。

除了要整理名称和表格美化以外，还要对成绩按照如下规则进行排序：
1. 按照成绩由高到低。
2. 当成绩相同时，按照姓名的首字母的字母序（忽略大小写）从小到大。
3. 当首字母相同时，以姓名长度（使用len函数）从短到长。
你应当比AI做得更好吧，不是吗？



输入：
第一行一个整数n，表示学生人数，n<=100.
接下来n行，每一行依次输入学生的姓名、成绩，以不确定数量的空格间隔。
姓名保证为为一个英文单词，由26个字母的大小写构成。不保证首字母大写。如果有重名保留第一条记录。
成绩为一个0到100之间的整数。

输出：
一个表格，以制表符Tab('\t')为间隔进行表格内容输出，表头分别为“Name”、“Score”。
输出名字的首字母大写，后续字母为小写。输出的成绩为整数。
'''

n = int(input())
scores = []
name_dict = {}
for i in range(n):
    name, score = input().split()
    name = name.capitalize() # 首字母大写，其余小写
    if name in name_dict: # 剔除重名
        continue
    name_dict[name] = score
scores = sorted(name_dict.items(), key=lambda x: (-int(x[1]), x[0][0], len(x[0])))
# 排序规则：成绩由高到低，姓名首字母从小到大，姓名长度从短到长
with open('./out/2.out', 'w', encoding='utf-8') as f:
    print("Name\tScore", file=f)
    for name, score in scores:
        print("{}\t{}".format(name, score), file=f)

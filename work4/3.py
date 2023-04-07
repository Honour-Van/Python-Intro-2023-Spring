# 照抄题目给出的模板代码
grade = []
n = int(input())
for i in range(n):
    grade.append([float(g) for g in input().split(" ")]) 
    
# 遍历对每行进行求和
for i in range(n):
    s = sum(grade[i])
    print(f'{s:.1f}', f'{s/3:.1f}') # 多种输出方式参考作业1的实例代码，这里使用f-string
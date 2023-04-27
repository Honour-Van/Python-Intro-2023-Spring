# 非匿名函数排序 基于#39597248 
# @credit 2000015176
# @fixed fhn

n = int(input())
records = []
for i in range(n):
    name, score = input().split()
    name = name.capitalize()
    if name not in [record[0] for record in records]:
        records.append((name.capitalize(), int(score)))
def sort_rule(record):
    name, score = record
    return (-score, name[0], len(name))

sorted_records = sorted(records, key=sort_rule)

print("Name\tScore")
for record in sorted_records:
    print(record[0]+"\t"+str(record[1]))
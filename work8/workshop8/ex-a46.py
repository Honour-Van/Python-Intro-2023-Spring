def average(ls):
    return sum(ls) / len(ls)

n = int(input())
mark_dict = {}
for i in range(n):
    word, grade = input().split()
    grade = int(grade)
    mark_dict[word] = mark_dict.get(word, []) + [grade]

ls = sorted(mark_dict.items(),key=lambda x:(-average(x[1]),-len(x[1]),x[0]))

for key, value in ls:
    print('{:.2f}'.format(average(value)), len(value), key)
# 字典值的一转多
# @credit 2100014928Cinderella

#n名学生
n = int(input())
dic = {}
#用字典记录学生数据
for i in range(n): #每行数据
    name,grade = input().split()
    name = name.title()
    grade = int(grade)
    lens = len(name)
    if name in dic.keys():
        continue
    else:
        dic[name] = [grade,lens]
#排序(此时已经是列表了！！）#第一排序码：成绩（降序） 第二排序码：当成绩相同时，按照姓名首字母升序 第三排序码：当首字母相同，按姓名长度升序
dic = sorted(dic.items(),key = lambda x: (-x[1][0],x[0][0],x[1][1])) #第一次注意首字母！而不是按照每个字符依次比较！

print('Name\tScore')
for i in range(len(dic)):
    print(dic[i][0],dic[i][1][0],sep='\t',end='\n')
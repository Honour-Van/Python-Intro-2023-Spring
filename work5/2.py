m,n=input().split()
m,n=int(m),int(n)
first_column=0
last_column=0
line_num=0
line=[]
s=0
if n>2 and m>2:
    for i in range(0,m):
        list1=list(map(int,input().split()))
        first_column+=list1[0]
        last_column+=list1[n-1]
        for j in range(1, n - 1):
            line_num += list1[j]
        line.append(line_num)
        line_num = 0
    print(first_column + last_column + line[0] + line[m - 1])
else:
    for i in range(0,m):
        list1=list(map(int,input().split()))
        for j in list1:
            s=s+j
    print(s)
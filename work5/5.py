t = int(input())
ls = []
for h in range(1,t+1):
    ls.append([h]*h)
for i in range(2,t): 
    for j in range(1,i):
        ls[i][j] = ls[i-1][j-1] + ls[i-1][j]
for i in range(t):
    print(ls[i])
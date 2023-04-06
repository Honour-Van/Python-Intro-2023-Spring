grade = []
n = int(input())
for i in range(n):
    grade.append([float(g) for g in input().split(" ")]) 
    
for i in range(n):
    s = sum(grade[i])
    print(f'{s:.1f}', f'{s/3:.1f}')
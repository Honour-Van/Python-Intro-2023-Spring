n = int(input())
stat = {}

def calc_timedelta(a, b):
    return (int(b[0:2]) - int(a[0:2])) * 3600 + (int(b[3:5]) - int(a[3:5])) * 60 + (int(b[6:8]) - int(a[6:8]))

for i in range(n):
    line = input().split()
    time = calc_timedelta(line[1], line[2])
    stat[line[0]] = stat.get(line[0], 0) + time
    
print(max(stat, key=stat.get))
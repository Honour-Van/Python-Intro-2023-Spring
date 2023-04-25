def add_line():
    D = {}
    line = input().split(',')
    for sec in line:
        secs = sec.split()
        D[secs[0]] = int(secs[1])
    return D

D = add_line()
D.update(add_line())

y3 = int(input())
D['a'] = y3

for i in ['c' in D, 0 in D.values(), ('b', 1) in D.items()]:
    print(str(i))

m, n = input().split()
m, n = int(m), int(n)
dishes = {} #菜品字典
s = []
for i in range(m+n):  # 输入m+n次
    info = input().split()
    name = info[0]
    num = info[1]
    dishes[name] = dishes.get(name,0)+int(num)
dishesnum = len(dishes.keys())
s = sorted(dishes.items(),key=lambda x:-x[1])
print(dishesnum)
for item in s:
    print(item[0], item[1])
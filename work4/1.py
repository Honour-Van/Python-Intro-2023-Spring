# @author:fhn
L = [int(i) for i in input().split(" ")]  # 获取列表
xy = input().split()
x = int(xy[0])  # 整数 x
y = int(xy[1])  # 整数 y

# step1:
L.insert(1, x)
# print(L.insert(1, x))  # None
print(L)

# step2:
L.pop(0)
print(L)

# step3:
del L[:3]
print(L)

# step4:
if 0 in L:
    print(True)
else:
    print(False)

# step5:
L.append(y)
print(L)

# step6:
print(len(L))

# step7:
print(max(L))
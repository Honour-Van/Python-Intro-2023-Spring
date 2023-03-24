# 采用陈徐磊同学的bing结果

sides = list(map(int, input().split()))
is_triangle = True
#用for循环遍历每个元素
for side in sides:# 如果当前元素大于或等于其他两个元素之和
    if side >= sum(sides) - side:# 不能组成一个三角形
        is_triangle = False
        break
# 根据结果输出信息
if is_triangle:
    print("yes")
else:
    print("no")

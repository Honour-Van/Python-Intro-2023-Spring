# 采用陈徐磊同学的bing结果
# 输入三个正整数，用空格隔开
a, b, c = map(int, input().split())
# 检查是否满足三角形不等式定理
if a + b > c and a + c > b and b + c > a:
    # 可以组成一个三角形
    print("yes")
else:
    # 不能组成一个三角形
    print("no")

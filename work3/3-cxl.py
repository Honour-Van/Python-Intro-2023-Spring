# @file: 3.py
# @credit: 陈徐磊

# 当距离小于100米时走路更快，大于100米则骑车更快。只需要定义一个比大小的函数即可：
def comp(n): # 函数的语法，在此定义，循环中调用
    if n > 100:
        print("Bike")
    elif n < 100:
        print("Walk")
    else:
        print("All")


# 输入项数：
m = int(input())
# 定义一个空列表，用来容纳将要输入路程数据：
dst = []
# 使用一种先保存再计算的思路，根据输入的项数m向列表中添加数据
for i in range(m):
    dst.append(int(input()))
# 开始处理列表中的数据：
for j in range(m):
    comp(dst[j])
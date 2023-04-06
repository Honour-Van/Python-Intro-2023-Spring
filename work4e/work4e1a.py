# @credit: 2200015498

listA = input().split()  # 一个input对应一行输入
listB = input().split()

num = len(listA)
output = []

for i in range(1, num+1):
    # i 一定和对应循环中的range值保持一致 [a, b)
    # range第一次的时候，i一定就是a
    # 第二次的时候i一定是a+1
    #
    # 问题：最先开始多输出了一个空格
    # 每句话有n个分节，2n-1 个空格
    # 方法2：先存成列表
    output.append(listB[-i])
    output.append(listA[-i])

# 输出法1：特判
# print(output[0])
# for item in output[1:]:
#     print(' ' + item, end='')

# 输出法2：特判2
# for item in output[:-1]:
#     print(item, end=' ')
# print(output[-1])

# 输出法3：使用join函数

print(' '.join(str(i) for i in output))

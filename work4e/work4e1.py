# @credit: 2200015498

listA = input().split()  # 一个input对应一行输入
listB = input().split()

num = len(listA)
output = ""

for i in range(1, num+1):
    # i 一定和对应循环中的range值保持一致 [a, b)
    # range第一次的时候，i一定就是a
    # 第二次的时候i一定是a+1
    #
    # 问题：最先开始多输出了一个空格
    # 每句话有n个分节，2n-1 个空格
    # 方法1：条件分支
    if i == 1:
        output = output + listB[-i] + " " + listA[-i]
    else:
        output = output + " " + listB[-i] + " " + listA[-i]
print(output)

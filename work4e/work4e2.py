# @credit: 2100014912

# 输入法1：列表生成式
# my_list = [int(i) for i in input().split()]

# 输入法2：简单的循环
pre_my_list = input().split()
for i in range(len(pre_my_list)):
    pre_my_list[i] = int(pre_my_list[i])
my_list = pre_my_list

a = int(input())
for i in range(a):
    b, c = input().split()
    # 等号左边也可以直接用一个变量line来替代
    # line 在这个情境下b = line[0], c = line[1]

    c = int(c)
    if b == "Append":
        my_list.append(c)
    elif b == "Delete":
        my_list.pop(c)  # pop 删除指定索引处的元素
                        # remove 是查找类的接口
    elif b == "Modify":
        # my_list.remove(my_list[-1])
        my_list.pop()  # 一个替代的简洁方案
        my_list.append(c)
        # 方法2：原位改变
        my_list[-1] = c

my_list.sort(reverse=True)

print(' '.join(str(i) for i in my_list))

# @file: 2-basic.py 基本版：遍历统计
# @author: fhn

s = input() # 直接输入就是字符串
num = 0
for i in s: # 遍历字符串会遍历每一个字符
    if i.isdigit(): # 利用函数检查是否为数字
        num = num + 1  
print(num)
# @file: 2-str_count.py 进阶版：使用str.count 函数
# @author: fhn

s = input()
ans = 0
for i in [str(x) for x in range(10)]: # 遍历这个列表生成式相当于遍历 '0123456789' 这个字符串
    ans += s.count(i)                 # 轮流统计每个字符在原串中的次数
print(ans)

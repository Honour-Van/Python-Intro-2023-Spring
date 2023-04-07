# 本题的一题多解可以参考例题参考程序，这里只给出两种解法

words = input().split()

words.reverse() # 先将列表反转，然后每两个取一个即可完成题目

n = len(words)
sentence1 = []
sentence2 = []
for i in range(0, n, 2):
    sentence1.append(words[i])
for i in range(1, n, 2):
    sentence2.append(words[i])

# 本题似乎不限制末尾的空格
for word in sentence1:
    print(word, end=' ')
print() # 相当于print('', end='\n) 自动换行

for word in sentence2:
    print(word, end=' ')